import threading
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7888))
    except:
        return print('Houve problema na tentatia de conexao')
    

    username = input('\nNome do usuario> ')
    print(f'{username} conectado com sucesso')

    thread1 = threading.Thread(target=receiveMessage,args=[client])
    thread2 = threading.Thread(target=sendMessage,args=[client, username])

    thread1.start()
    thread2.start()

def receiveMessage(client):
    while True:

        try:
            msg = client.recv(1024).decode('utf-8')
            print(msg+'\n')
        except:
            print(f"o usuario {client} saiu")
            client.close()
            break

def sendMessage(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return
main()