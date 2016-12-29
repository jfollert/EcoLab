from socket import *

print "Creando socket..."
s = socket(AF_INET, SOCK_STREAM)

print "Socket:", s

host = gethostname()
print "Hostname:", host
#ip = raw_input("Ingresa una ip para el socket: ")
port_c = int(raw_input("Ingresa un puerto para el socket: "))

print "Asociando datos..."
s.bind((host, port_c))


print "Escuchando puerto... "
s.listen(10)


while 1:
    print "ciclo"
    add, port = s.accept()
    add.send("Conectado con el servidor " + host + " por el puerto " + str(port_c))
    print add.recv(255)
