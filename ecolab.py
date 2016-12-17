# MODULES #
from argprocess import ArgsProcess
import socket
import sys
import os
import time
import struct
# STATIC VARIABLES #
nm = __file__
# CMD FUNCTIONS #
## HELP
def help(cmd="0"):
    helpDic = { "connect": "Use connect: \n\t" + nm + " connect [IP] [PORT] (port default = 5678)",
               "wake" : "Use wake: \n\t" + nm + " -a [For Wake all]  / -i [IP]"}
    if cmd == "0": #default help
        for com in helpDic.values():
            print com
    else:
        print helpDic[cmd]

## WAKE
def wake(ip):
    print "Enviando paquete magico a:", ip #(EN) Sending magic packet to: IP
    mac = arp[ip]
    print "MAC:", mac
    wakeOnLan(mac)
    """
    time.sleep(2)
    while i == 20:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (ip, int(port))
            sock.connect(server_address)
        except:
            pass
    """

## CONNECT
def connect(ip, port):
    print "Intentando conexion a", ip + ":" + port #(EN) Trying connection to IP:Port
    tryConnect(ip, port)
    time.sleep(2)
    sendCmd(sock)
    time.sleep(5)

###### OTHER FUNCTIONS
## READ DATA
def leerArp():
    arch = open("data/arp.dat") #arp.dat is an ethernet/ip address database
    for linea in arch:
        linea = linea.strip().split("-")
        #print linea
    arch.close()

## WAKEONLAN
def wakeOnLan(macaddress):
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 12 + 5:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Formato de MAC incorrecto!') #(EN) Incorrect MAC format!

    data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
    send_data = ''

    for i in range(0, len(data), 2):
        send_data = ''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, ('<broadcast>', 7))

## SEND CMD
def sendCmd(sock):
    while True:
        cmd = raw_input("camando->") #se ingresa por teclado el comando que deseamos # (EN) Gets command from user
        sock.send(cmd)#enviamos el comando  # (EN) Sends the command
        time.sleep(2)
        output = sock.recv(100000)#recibimos la salida # (EN) Receives output
        print output #se imprime por pantalla la salida # (EN) Prints output

## TRY CONNECT
def tryConnect(ip, port):
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, int(port))
        sock.connect(server_address)
    except socket.error:
        print "[ERROR] No se pudo establecer conexion con el servidor" # (EN) Could not establish a connection to the server

###### ARGS
if __name__ == "__main__":
    try:
        os.system("clear")
    except:
        pass

    args =  ArgsProcessClient(__file__)
