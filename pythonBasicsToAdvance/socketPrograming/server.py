import socket

s = socket.socket()
print("socket created")
s.bind(("localhost" , 9999))

s.listen(3)

print("waiting for connection")

while True:
    c ,addr = s.accept()
    name = c.recv(1024).decode()
    print("connection with :" ,addr,name)
    c.send("message from server side".encode())
    c.close()