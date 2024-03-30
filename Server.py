from socket import *

s = socket()
print("\nCreated Socket...")

s.bind(('localhost',9998))

s.listen(3)
print("\nWaiting for connections...")

while True:

    c , add = s.accept()
    name = c.recv(1024).decode()

    print(f"\nConnected with client {add} -----> {name}")

    c.send(bytes("Hello World...","utf-8"))

    c.close()
