import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = raw_input("Enter the name of the host: ")
port = int(raw_input("Enter its port: "))
client.connect((host, port))

print client.recv(255)
client.send("hello")
client.close()
