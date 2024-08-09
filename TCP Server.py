import socket


#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444 

serversocket.bind((host, port))

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection 
    clientsocket,address = serversocket.accept()

    print("received connection from: %s " % str(address))
    
    #Message sent to client after successful connection
    message = 'hello! Thank you for connecting to the server' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
