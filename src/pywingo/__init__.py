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
        self.__sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        f = os.path.join(os.getenv('XDG_RUNTIME_DIR'), 'wingo',
                         os.getenv('DISPLAY'))
        self.__sock.connect(f)
        self.__buf = ''

    def __del__(self):
        self.__sock.close()

    def __recv(self):
        while chr(0) not in self.__buf:
            self.__buf += self.__sock.recv(4096)

        sentinel = self.__buf.index(chr(0))
        payload = self.__buf[0:sentinel][:]
        self.__buf = self.__buf[sentinel+1:]
        return payload

    def gribble(self, cmd):
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

