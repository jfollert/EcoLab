# MODULES #
import sys
import socket
import os
import time
import struct

# STATIC VARIABLES #
nm = __file__


# CMD FUNCTIONS #
def help(cmd="0"):
    help_dic = {
        "connect": "Use connect: \n\t" + nm + " connect [IP] [PORT] (port default = 5678)",
        "wake": "Use wake: \n\t" + nm + " -a [For Wake all]  / -i [IP]"
    }

    # default help
    if cmd == "0":
        for com in help_dic.values():
            print com
    else:
        print help_dic[cmd]


def wake(ip):
    print "Sending packets to:", ip  # (EN) Sending magic packet to: IP
    mac = arp[ip]
    print "MAC:", mac
    wake_on_lan(mac)
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
    # (EN) Trying connection to IP:Port
    print "Trying connection to", ip + ":" + port
    try_connection(ip, port)
    time.sleep(2)
    send_cmd(sock)
    time.sleep(5)


def read_arp():
    # arp.dat is an ethernet/ip address database
    arch = open("data/arp.dat")

    for line in arch:
        line = line.strip().split("-")
        print line
    arch.close()


def wake_on_lan(mac_address):
    if len(mac_address) == 12:
        pass
    elif len(mac_address) == 12 + 5:
        sep = mac_address[2]
        mac_address = mac_address.replace(sep, '')
    else:
        raise ValueError('Wrong MAC Address format!')  # (EN) Incorrect MAC format!

    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])
    send_data = ''

    for i in range(0, len(data), 2):
        send_data = ''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(send_data, ('<broadcast>', 7))


def send_cmd(s):
    while True:
        # Se ingresa por teclado el comando que deseamos
        # (EN) Gets command from user
        cmd = raw_input("command->")

        # enviamos el comando
        # (EN) Sends the command
        s.send(cmd)

        time.sleep(2)

        # recibimos la salida
        # (EN) Receives output
        output = sock.recv(100000)

        # se imprime por pantalla la salida
        # (EN) Prints output
        print output


def try_connection(ip, port):
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, int(port))
        sock.connect(server_address)
    except socket.error:
        print "[ERROR] Could not establish a connection to the server"


###### ARGS
if __name__ == "__main__":
    try:
        os.system("clear")
    except:
        pass

    args = ArgsProcessClient(__file__)
