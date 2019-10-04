from socket import *

print "Creating socket..."
s = socket(AF_INET, SOCK_STREAM)

print "Socket:", s

host = gethostname()
print "Hostname:", host

# ip = raw_input("Ingresa una ip para el socket: ")

port_c = int(raw_input("Enter a port for the socket: "))

print "Associating..."
s.bind((host, port_c))

print "Listening on port ", str(port_c), " ..."
s.listen(10)

while 1:
    # Not sure about the next line's translation
    print "Cycling"
    add, port = s.accept()
    add.send("Connected to server " + host + " on port " + str(port_c))
    print add.recv(255)
