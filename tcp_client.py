import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

client.send("Olá Servidor!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
client.send("Tchau!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))