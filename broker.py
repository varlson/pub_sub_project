from http import client
import threading
import socket
clients = []
class Broker:
    def __init__(self, port, hostname):
        self.port = port
        self.hostname = hostname
        self.client = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind((self.hostname, self.port))
            self.server.listen()
            print('Broker conectado no host {} e na porta {}'.format(self.hostname, self.port))

        except:
            return print('\n Não possivel iniciar o servidor')
    
        while True:
            self.client, self.addr = self.server.accept()
            clients.append(self.client)
            thread = threading.Thread(target=self.messageTreatment)
            thread.start()
    
    def messageTreatment(self):
        while True:
            try:
                msg = self.client.recv(1024)
                self.broadcast(msg)
            except:
                self.deleteClient(self.client)
                break
    def broadcast(self, msg):
        for cli in clients:
            if cli != self.client:
                try:
                    self.server.send(cli)
                except:
                    self.deleteClient(cli)     
    def deleteClient(self, cli):
        clients.remove(cli)


broker = Broker(8080, 'localhost')