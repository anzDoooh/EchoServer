#client socket
import socket
from pickle import dumps,loads

x = socket.socket()
port, host = 5000, '127.0.0.1'
x.connect((host, port))

"""
data=dumps([x for x in "Hello World..!"])
x.sendall(data)
x.sendall(b":>Hey.. I'm client, connected with you...") #send string to server(byte format)
#run while the server is running for connecting
"""

ch ='1'
while(ch!='#'):
    print("Enter data to send")
    data = input()
    x.sendall(dumps(data))

