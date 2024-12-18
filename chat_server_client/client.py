import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(f"Mensagem recebida: {message}")
        except:
            print('Conexão encerrada')
            client.close()
            break

def send_messages(client):
    while True:
        try:

            message = str(input('Escreva a Mensagem: '))
            client.send(message.encode())
        except:
             break
        
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f'Conectado ao servidor IPV4: {HOST}, na porta: {PORT}')

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    send_messages(client)

if __name__ == '__main__':
    main()