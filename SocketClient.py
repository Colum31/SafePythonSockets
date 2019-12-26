import socket
import time

s = socket.socket()

ip = '127.0.0.1'
port = 12345
connected = False

while connected == False:      # ^
    try:

        s.connect((ip, port))
        connected = True

    except socket.error:
        print("Could not connect to %s:%s" % (ip, port))
        print "Retrying"
        time.sleep(2)


while True:
    try:

        print "Send:",

        message = raw_input()

        if message == "":
            message = " "

        s.send(message)
        print("----------\nSent: %s" % (message))

        data = s.recv(1024)
        print"Received: %s" % (data)

        if data == "bye m8":
            print("Server closed the connection")
            break



    except socket.error:
        print("Socket Error: Server disconnected?")
        break

s.close()
