from concurrent.futures import thread
from email import message
from pydoc import cli
import threading
import socket

from numpy import broadcast

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('localhost', 7888))
        server.listen()
        print('Server online ')
    except:
        return print('Houve prolema na conexao')
        
    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messageTreatment, args=[client])
        thread.start()

def messageTreatment(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            clients.remove(client)
            break

def broadcast(msg, client):
    for cli in clients:
        if cli != client:
            try:
                cli.send(msg)
            except:
                clients.remove(cli)

main()