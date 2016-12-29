import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input("Ingrese el nombre del host: ")
port = int(raw_input("Ingrese el puerto: "))
cliente.connect((host, port))
print cliente.recv(255)
cliente.send("hola")
cliente.close()
