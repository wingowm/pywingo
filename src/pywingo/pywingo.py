import os
import os.path
import socket


class Wingo(object):
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
