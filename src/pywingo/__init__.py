import json
import os
import os.path
import socket
import time

from pywingo.commands import WingoCommands
import pywingo.events as events

_bool_cmds = ['True', 'False', 'Not', 'And', 'Or']

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


class _wingoUtil(WingoCommands):
    '''
    Provides a set of utility functions on top of the base commands
    defined by Wingo. These are special to the Python Wingo bindings.
    '''
    def __init__(self):
        assert False, 'cannot create WingoCommands directly'

    def IsEmpty(self, Workspace):
        '''
        Returns true if the given Workspace has no clients. (Including
        iconified clients.)

        Workspace may be a workspace index (integer) starting at 0, or a 
        workspace name.
        '''
        return len(self.GetClientList(Workspace)) == 0


class Wingo(_wingoUtil):
    def __init__(self):
        self.__sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        f = os.path.join(os.getenv('XDG_RUNTIME_DIR'), 'wingo',
                         os.getenv('DISPLAY'))
        self.__sock.connect(f)
        self.__buf = ''
        self.__evbuf = ''
        self.__callbacks = { }

        # Not opened until the event loop is started.
        self.__evsock = None

    def __del__(self):
        self.__sock.close()

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
        Otherwise, use the API to run commands.
        '''
        self.__sock.send("%s%s" % (cmd, chr(0)))
        return self.__recv()

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
                args.append('"%s"' % self._escape_str(v))
            else:
                assert False, 'bug'
        return ' '.join(args)

    def _escape_str(self, s):
        return s.replace('"', '\\"')

    def _from_str(self, cmd_name, s):
        if cmd_name in _bool_cmds or cmd_name.startswith('Match'):
            return bool(int(s))

        if 'List' in cmd_name or '\n' in s:
            trimmed = s.strip()
            if len(trimmed) == 0:
                return []
            return map(lambda item: self._primitive_from_str(cmd_name, item),
                       trimmed.split('\n'))

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

        try:
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                return s

        assert False, 'bug'

    def loop(self, restart=True):
        '''
        Listens for event notifications and executes callbacks when
        corresponding events are received.

        When `restart` is enabled, the event loop will be restarted if there
        was an error reading from the socket. This is intended to keep the
        program alive if Wingo restarts. (If Wingo really does die, the
        reconnection will fail and a regular socket error will be raised.)
        '''
        try:
            self.__evsock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            f = os.path.join(os.getenv('XDG_RUNTIME_DIR'), 'wingo',
                             os.getenv('DISPLAY') + '-notify')
            self.__evsock.connect(f)
            
            while True:
                evJson = self.__recv_event()
                j = json.loads(evJson)
                ev_name = str(j['EventName'])
                ev = events.__dict__['_new_%s' % ev_name](j)

                for cb in self.__callbacks.get(ev_name, []):
                    cb(ev)
        except Disconnected:
            if not restart:
                raise Disconnected
            time.sleep(1)
            self.loop(restart)

    def bind(self, event_name, f):
        '''
        Binds an event named `event_name` to a callback function `f`.
        `f` should be a function that takes a single argument `event`,
        which will correspond to a namedtuple of the event with any
        relevant data as properties.
        '''
        if event_name not in self.__callbacks:
            self.__callbacks[event_name] = []
        self.__callbacks[event_name].append(f)

