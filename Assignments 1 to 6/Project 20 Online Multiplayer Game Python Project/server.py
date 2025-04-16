import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            clients.remove(client)
            client.close()
            break

print("Server running...")
while True:
    client, addr = server.accept()
    print(f"Connected with {addr}")
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
