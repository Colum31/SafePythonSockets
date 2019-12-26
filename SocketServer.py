import socket

bufferCount = 1     # generates value for buffer
bufferSize = 0      # number of entries in buffer messageBuffer = ""
lastMessage = ""    # contains the last received message
respond = ""        # stores the respond to be sent

def messageParser(input):       # parses received message and decides what to respond

    global bufferSize
    global bufferCount
    global messageBuffer
    global c

    global respond

    operation = input[0]      # takes first character of the message

    if operation == 'a':      # first character decides what to respond
                              # a - [a]dds to Buffer
        bufferCount *= 2
        addToMessageBuffer(bufferCount)
        respond = "Value %s Appended to Buffer, current size: %s" %(bufferCount , bufferSize)

    elif operation == 'l':   # l - [l]ast received message will be sent back

       respond = "Last Message: %s" % lastMessage

    elif operation == 'c':  # c - [c]lears buffer

       respond = "Reseting Buffer!"
       resetBuffer()

    elif operation == 'p': # p - [p]ing

        respond = "Pong!"

    elif operation == 'x': # x - close the connection

        print("Kill Signal received!")
        respond = "bye m8"

    elif operation =='d':  # d - [d]isplay buffer
        respond = ("Pasting Buffer: %s; Buffersize: %s Entities" %(messageBuffer, bufferSize))

    else: # self explanatory

        respond = "Command unknown"

    c.send(respond)     # send the respond

def addToMessageBuffer(input):  # add the current value to Buffer , temporary development
                                # artifact for the establishment for a token system
    global bufferSize
    global messageBuffer

    bufferSize = bufferSize + 1 # increase next buffer input
    messageBuffer =+ input      # add input message to buffer

def resetBuffer():  # clears the buffer

    global bufferSize
    global bufferCount
    global messageBuffer

    bufferSize = 0     # resets all variables
    bufferCount = 1
    messageBuffer = ""


s = socket.socket()                                       # create socket and config
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket created!")

ip = '127.0.0.1'     # settings for socket
port = 12345

s.bind((ip, port))   # bind socket to settings above
print ("Socket on %s:%s" % (ip, port))

s.listen(1)   # waits until a client connects

c , addr = s.accept()   # all inbound are being accepted
                        # c - new socket ; addr - tuple with ip and port of client

print ("Inbound connection from: %s : %s" % (addr[0], addr[1]))

while True:
    data = c.recv(1024)     # reads from c and stores it in a buffer (not the variable)

    print "Received: %s" %data

    messageParser(data)    # processes received message
    lastMessage = data     # stores received message

    print("Sent: %s" % respond)

    if respond == "bye m8":  # if kill signal was received program termiantes
        s.close()
        exit(0)
        break;

c.send("unknown mistake")   # should be unreachable
s.close()
exit(-2)
