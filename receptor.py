# -*- coding: utf-8 -*-
# Camada Física da Computação
# Exemplo socket server 
## https://pymotw.com/2/socket/tcp.html

import socket

class Receptor:
    def __init__(self):
        self.port = 1234
        self.busy = False
        self.connection = None
        self.connected = False
        self.buffer = []

    def connect(self):
        """ Returns true if connection is successful """
        print("[Receptor] Inicializando socket TCP/IP")
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', self.port)
        print("[Receptor] PORTA {}".format(self.port))
        sock.bind(server_address)
        # Listen for incoming connections
        sock.listen(1)

        while True:
            # Wait for a connection
            print("[Receptor] waiting for a connection")
            self.connection, self.client_address = sock.accept()
            self.connected = True
            return self.connected

    def listen(self):
        string = ''
        print('[Receptor] CHEGUEI AQUI')
        try:
            print("[Receptor] connection from {}".format(self.client_address))

            # Receive the data in small chunks and retransmit it
            while True:
                print('Listening...')
                char = str(self.connection.recv(16),'utf-8')
                print(char)

                if char == '&':
                    print('[Receptor] found head')
                    self.busy = True

                elif char == '|' and self.busy == True:
                    print('[Receptor] found EOP')
                    received = string
                    string = ''
                    self.busy = False
                    print('[Receptor] Received string',received)
                    self.buffer.append(received)

                if self.busy == True and char != '&' and char != '|':
                    string += char
    
                # print("{}".format(string))
                # if(len(data) <= 0):
                #     break
        except:
            print('Deu ruim na listen thread')
            self.listen()

        #     # Clean up the connection
        #     self.connection.close()
        
    def getBuffer(self):
        if len(self.buffer) > 0:
            buffer = self.buffer
            self.buffer = []
            return buffer
        else:
            return None