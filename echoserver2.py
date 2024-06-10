#server socket
import socket #socket module input
from pickle import dumps,loads # TODO
# threading have to importdxcf
#define a function for continous recieving
"""client-server one way connection"""
def recv_from_client():
    global conn, connected
    while(connected):
        data = conn.recv(1024)
        print("Client data>",loads(data))


x = socket.socket() #socket itnitializing as default socket
port , host = 5000, '127.0.0.1' # definbe the port & host
x.bind((host, port)) #asscociate the port with the host
x.listen(2) #waite until a client's joining(count of clients)
#listening is a blocking call

"""
conn - socket object
addr - addres of them
"""

conn, addr = x.accept() #connect the client with the host

connected = True

"""
print("\nconnected successsfully...\n\n","details:",(conn, addr))

data = conn.recv(1024)
print("\nclient's>" , data)
"""

recv_from_client()
# x.close()

