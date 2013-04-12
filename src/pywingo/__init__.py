import os
import os.path
import socket

from pywingo.commands import WingoCommands

_bool_cmds = ['True', 'False', 'Not', 'And', 'Or']

class WingoError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Wingo(WingoCommands):
    def __init__(self):

        # Open socket
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        f = os.path.join(os.getenv('XDG_RUNTIME_DIR'), 'wingo',
                         os.getenv('DISPLAY'))
        self.sock.connect(f)

    def __del__(self):
        # Close socket
        self.sock.close()

    def __recv(self, sock):
        data = ''
        while chr(0) not in data:
            data += sock.recv(4096)
        if chr(0) in data:
            data = data[0:data.index(chr(0))]
        return data

    def gribble(self, cmd):
        self.sock.send("%s%s" % (cmd, chr(0)))
        return self.__recv(self.sock)

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

        try:
            return int(s)
        except ValueError:
            try:
                return float(s)
            except ValueError:
                if s.startswith('ERROR:'):
                    raise WingoError(s)
                elif '\n' in s:
                    return map(lambda item: self._from_str(cmd_name, item),
                               s.strip().split('\n'))
                else:
                    return s

        assert False, 'bug'

