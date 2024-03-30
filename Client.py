from socket import *

c = socket()
print("\nCreated socket...\n")

c.connect(('localhost',9998))

name=input("Enter ur name: ")
c.send(bytes(name,'utf-8'))

msg = c.recv(1024)
print(msg.decode(),"\n")
