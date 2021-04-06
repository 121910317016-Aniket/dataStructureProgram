import socket
c=socket.socket()
c.connect(('LocalHost',9999))
c.send(bytes("Aniket",'utf-8'))

print(c.recv(1024).decode())