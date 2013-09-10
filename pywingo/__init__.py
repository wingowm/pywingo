"""
Module pywingo provides a high level interface to the
[Wingo](https://github.com/BurntSushi/wingo) window manager. This
includes running commands to manage your windows and workspaces, and
responding to events sent by Wingo.
"""
import ConfigParser
import json
import os
import os.path
import socket
import subprocess
import sys
import tempfile
import time

from pywingo.commands import WingoCommands
import pywingo.events as events

__all__ = ['Wingo', 'WingoError', 'Disconnected', 'events']

_bool_cmds = ['True', 'False', 'Not', 'And', 'Or']
_string_cmds = ['GetWorkspace', 'GetWorkspaceList',
                'GetWorkspaceNext', 'GetWorkspacePrev', 'GetWorkspacePrefix',
                'GetHeadWorkspace', 'GetClientWorkspace']
_list_cmds = ['GetAllClients']


class WingoError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Disconnected(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'socket disconnected'


class WingoUtil(WingoCommands):
    '''
    Provides a set of utility functions on top of the base commands
    defined by Wingo. These are special to the Python Wingo bindings.
    '''
    def __init__(self):
        assert False, 'cannot create WingoCommands directly'

    def GetAllNormalClients(self):
        '''
        Exactly the same as GetAllClients, except only clients with
        type "normal" are returned. (i.e., excludes "desktop" and
        "dock" clients.)
        '''
        cids = []
        for cid in self.GetAllClients():
            if self.GetClientType(cid) == 'normal':
                cids.append(cid)
        return cids

    def IsEmpty(self, Workspace):
        '''
        Returns true if the given Workspace has no clients. (Including
        iconified clients.)

        Workspace may be a workspace index (integer) starting at 0, or a
        workspace name.
        '''
        return len(self.GetClientList(Workspace)) == 0

    def GetVisibleWorkspaceList(self):
        '''
        Returns a list of all visible workspaces in order of their
        physical position: left to right and then top to bottom.
        '''
        spaces = []
        for i in xrange(self.GetNumHeads()):
            spaces.append(self.GetHeadWorkspace(i))
        return spaces

    def GetHiddenWorkspaceList(self):
        '''
        Returns a list of all hidden workspaces.
        '''
        spaces = []
        visibles = set(self.GetVisibleWorkspaceList())
        for space in self.GetWorkspaceList():
            if space not in visibles:
                spaces.append(space)
        return spaces

    def LoadConfig(self):
        '''
        Returns a ConfigParser.RawConfigParser instance of your
        script-name.cfg file. This should only be used inside a
        Wingo contrib script program.

        If the config file is not readable, then the program will
        terminate with an error message.
        '''
        fname = os.path.basename(sys.argv[0])
        cfg_path = self.ScriptConfig(fname)
        if not os.access(cfg_path, os.R_OK):
            print >> sys.stderr, "Could not read config file for %s" % fname
            print >> sys.stderr, "Please make sure there is a config file " \
                                 "in ~/.config/wingo/scripts/%s" % fname
            sys.exit(1)

        cfg = ConfigParser.RawConfigParser()
        cfg.read(cfg_path)
        return cfg


class Wingo(WingoUtil):
    def __init__(self, display=None):
        '''
        Initializes a connection with an instance of Wingo.
        Once a connection has been established, commands can be
        executed.

        If `display` is not set, then pywingo will try to find the
        current instance of Wingo and connect to that. This is almost
        always what you want, unless you know you need to connect to
        an instance of Wingo from within a different X session (or no
        X session at all).

        If `display` is set, then it *must* be in the following format:

        :{X Server}.{X Screen}

        e.g., `:0.0` or `:11.1`.

        Any other format is invalid.
        '''
        self.__buf = ''
        self.__evbuf = ''
        self.__callbacks = {}

        # Not opened until the first command is issued.
        self.__sock = None

        # Not opened until the event loop is started.
        self.__evsock = None

        self.__path = _socket_filepath(display)

    def __del__(self):
        if self.__sock is not None:
            self.__sock.close()

    def __reconnect(self):
        self.__sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.__sock.connect(self.__path)

    def __recv(self):
        while chr(0) not in self.__buf:
            data = self.__sock.recv(4096)
            if not data:
                raise Disconnected
            self.__buf += data

        sentinel = self.__buf.index(chr(0))
        payload = self.__buf[0:sentinel][:]
        self.__buf = self.__buf[sentinel+1:]
        return payload

    def __recv_event(self):
        assert self.__evsock is not None

        # So far this is the same as `__recv`, but they use different
        # buffers and could potentially use different protocols.
        while chr(0) not in self.__evbuf:
            data = self.__evsock.recv(4096)
            if not data:
                raise Disconnected
            self.__evbuf += data

        sentinel = self.__evbuf.index(chr(0))
        payload = self.__evbuf[0:sentinel][:]
        self.__evbuf = self.__evbuf[sentinel+1:]
        return payload

    def gribble(self, cmd):
        '''
        Executes a raw Gribble commands and always returns the result
        as a string. This should only be used if you know it's necessary.
        Otherwise, use the API to run specific commands.
        '''
        try:
            self.__send_cmd(cmd)
            return self.__recv()
        except Disconnected:
            # Try again, just once.
            self.__send_cmd(cmd)
            return self.__recv()

    def __send_cmd(self, cmd):
        if self.__sock is None:
            self.__reconnect()
        try:
            self.__sock.send('%s%s' % (cmd, chr(0)))
        except:
            raise Disconnected

    def _assert_arg_type(self, name, val, types):
        for t in types:
            if isinstance(val, t):
                return
        assert False, '%s has invalid type %s' % (name, type(val))

    def _gribble_arg_str(self, vals):
        args = []
        for v in vals:
            if isinstance(v, int) or isinstance(v, float):
                args.append(repr(v))
            elif isinstance(v, basestring):
                args.append('`%s`' % self._escape_str(v))
            else:
                assert False, 'bug'
        return ' '.join(args)

    def _escape_str(self, s):
        return s.replace('"', '\\"')

    def _from_str(self, cmd_name, s):
        if cmd_name in _bool_cmds or cmd_name.startswith('Match'):
            return bool(int(s))

        if 'List' in cmd_name or '\n' in s or cmd_name in _list_cmds:
            trimmed = s.strip()
            if len(trimmed) == 0:
                return []
            return map(lambda item: self._primitive_from_str(cmd_name, item),
                       trimmed.split('\n'))

        if cmd_name in _string_cmds:
            return s

        try:
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                if s.startswith('ERROR:'):
                    raise WingoError(s)
                else:
                    return s

        assert False, 'bug'

    def _primitive_from_str(self, cmd_name, s):
        if cmd_name in _bool_cmds or cmd_name.startswith('Match'):
            return bool(int(s))

        if cmd_name in _string_cmds:
            return s

        try:
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                return s

        assert False, 'bug'

    def __wingo_restarting(self, ev):
        if self.__sock is not None:
            self.__sock.close()
        self.__sock = None

    def loop(self, restart=True):
        '''
        Listens for event notifications and executes callbacks when
        corresponding events are received.

        When `restart` is enabled, the event loop will be restarted if there
        was an error reading from the socket. This is intended to keep the
        program alive if Wingo restarts. (If Wingo really does die, the
        reconnection will fail and a regular socket error will be raised.)
        '''

        # Invalidate the Gribble socket once Wingo starts restarting.
        self.bind('Restarting', self.__wingo_restarting)

        try:
            self.__evsock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            f = os.path.join(self.__path + '-notify')
            self.__evsock.connect(f)

            while True:
                evJson = self.__recv_event()
                j = json.loads(evJson)
                ev_name = str(j['EventName'])
                key = '_new_%s' % ev_name
                if key not in events.__dict__:
                    print >> sys.stderr, \
                        'Event "%s" is not defined in pywingo. ' \
                        'Time to update!' % ev_name
                    continue
                ev = events.__dict__[key](j)

                for cb in self.__callbacks.get(ev_name, []):
                    cb(ev)
        except Disconnected:
            if not restart:
                raise Disconnected
            time.sleep(1)
            self.loop(restart)

    def bind(self, event_name, f=None):
        '''
        Binds an event named `event_name` to a callback function `f`.
        `f` should be a function that takes a single argument `event`,
        which will correspond to a namedtuple of the event with any
        relevant data as properties.

        If `f` is None, then a partially applied function is returned.
        (For decorator support.)
        '''
        def doit(fun):
            if event_name not in self.__callbacks:
                self.__callbacks[event_name] = []
            self.__callbacks[event_name].append(fun)
            return fun

        if f is None:
            return doit
        return doit(f)


def _socket_filepath(display=None):
    if display is not None:
        rundir = os.getenv('XDG_RUNTIME_DIR').strip()
        if len(rundir) == 0:
            rundir = tempfile.gettempdir()
        return os.path.join(rundir, 'wingo', display)

    try:
        fp = subprocess.check_output(['wingo', '--show-socket'],
                                     stderr=subprocess.STDOUT)
        return fp.strip()
    except subprocess.CalledProcessError, e:
        raise WingoError(e.output)
