import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))
client.send("Olá Servidor! Sou o cliente".encode())
resposta = client.recv(1024).decode()
print("Resposta do servidor:", resposta)
client.close()
