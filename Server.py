import socket
s=socket.socket()
print('Socket created ')
s.bind(('LocalHost',9999))
s.listen(3)
print('waiting for connection ')
while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print('Connected with {} {} '.format(addr,name))

    c.send(bytes('Welcome to server ','utf-8'))
    c.close()
