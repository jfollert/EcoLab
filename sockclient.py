import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input("Enter the name of the host: ")
port = int(raw_input("Enter its port: "))
cliente.connect((host, port))
print cliente.recv(255)
cliente.send("hola")
cliente.close()
