##### BasFO 2016 #####
###### MODULOS #######

import socket
import sys
import os
import time
import struct

###### ESTATICAS #####

nm = __file__
####### FUNCIONES DE ARGUMENTOS #######

def help(cmd="0"):
        helpDic = { "connect": "Uso connect: \n\t" + nm + " connect [IP] [PORT] (port default = 5678)", 
                   "wake" : "Uso wake: \n\t" + nm + " -a [For Wake all]  / -i [IP]"}
        if cmd == "0":
                for com in helpDic.values():
                        print com
        else:
                print helpDic[cmd]
                
def wake(ip):
        print "Enviando paquete magico a:", ip
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

def connect(ip, port):
        print "Intentando conexion a", ip + ":" + port
        tryConnect(ip, port)
        time.sleep(2)
        sendCmd(sock)
        time.sleep(5)

####### FUNCIONES GENERALES #########

def leerArp():
        arch = open("data/arp.dat")
        for linea in arch:
                linea = linea.strip().split("-")
                #print linea
        arch.close()

def wakeOnLan(macaddress):
        if len(macaddress) == 12:
                pass
        elif len(macaddress) == 12 + 5:
                sep = macaddress[2]
                macaddress = macaddress.replace(sep, '')
        else:
                raise ValueError('Formato de MAC incorrecto!')
        
        data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
        send_data = '' 

        for i in range(0, len(data), 2):
                send_data = ''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, ('<broadcast>', 7))
        
def  sendCmd(sock):
        while True:
                cmd = raw_input("camando->") #le damos entrada por teclado al comand que deseamos  
                sock.send(cmd)#enviamos el comando
                time.sleep(2)
                output = sock.recv(100000)#recibimos la salida
                print output #printeamos la salida


def tryConnect(ip, port):
        global sock
#try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, int(port))
        sock.connect(server_address)
#except socket.error:
        print "[ERROR] No se pudo establecer conexion con el servidor"

####### ANALISIS DE ARGUMENTOS ########
if __name__ == "__main__":
        leerArp()
        os.system("clear")
        
        if len(sys.argv) != 1: #Si existen argumentos
                if sys.argv[1] == "connect":
                        if len(sys.argv) > 2 and len(sys.argv) < 5:
                                #SI NO SE ESPECIFICA PUERTO, SE USA 5678 POR DEFECTO
                                if len(sys.argv) == 3:
                                        port = "5678"
                                elif len(sys.argv) == 4:
                                        port = sys.argv[3]
                                connect(sys.argv[2], port)
                        else:
                                if len(sys.argv) == 2:
                                        help("connect")
                                else:
                                        print "NO SE ACEPTAN TANTOS ARGUMENTOS"
                elif sys.argv[1] == "wake":
                        if len(sys.argv) > 2:
                                if sys.argv[2] == "-i":
                                        wake(sys.argv[3])
                                
        else: #Si no hay argumentos se imprime la ayuda
                help()

