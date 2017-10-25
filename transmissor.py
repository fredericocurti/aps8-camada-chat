import socket,sys

class Transmissor:
    def __init__(self):
        self.head = '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
        self.eop = '||||||||||||'
        self.port = 4321
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.sock.connect(('localhost',self.port))
        print('[Transmissor] Connecting transmissor to GNURadio to send text')

    def send(self,text):
        package = bytes(self.head, 'utf-8') + bytes(text, 'utf-8') + bytes(self.eop, 'utf-8')
        self.sock.send(package)
        print('[Transmissor] Text sent')