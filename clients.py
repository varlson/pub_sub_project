from http import client
import threading
import socket
import sys
from tracemalloc import start
class Clients:
    def __init__(self, hostname, port, name):
        self.port = port
        self.hostname = hostname
        self.name = name
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        try:
            self.client.connect((self.hostname, self.port))
            print('Usuario conectado no host {self.host} e na porta {self.port}')

        except:
            return print('\n Não possivel conectador ao servidor')
        thread1 = threading.Thread(target=self.sendMessage)
        thread2 = threading.Thread(target=self.receiveMessage)

        thread1.start()
        thread2.start()
    
    def receiveMessage(self):
        while True:
            try:
                msg = self.client.recv(1024).decode('utf-8')
                print(msg+'\n')
            except:
                print("\n Nao permanceu concetado\n")
                self.client.close()
                break

    def sendMessage(self):
        while True:
            try:
                msg = input('\n')
                self.client.send('<{self.name}> {msg}'.encode('utf-8'))
            except:
                return 




# if __name__ == 'main':
if len(sys.argv) <= 3:
    # print('entre com os parametros corretos\n', sys.argv)
    sys.exit()
# _client = Clients('localhost', 8080, 'Manito')
name = sys.argv[3]
port = int(sys.argv[2])
host = sys.argv[1]

# _client = Clients(host, port, name)
# _client.start()
