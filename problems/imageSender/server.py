import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',1025))
server.listen()

client_socket,client_address=server.accept()

f= open("/home/alex/Documents/problems/imageSender/sent.jpg","wb")
parca = client_socket.recv(1024)

while parca:
    f.write(parca)
    parca = client_socket.recv(1024)

f.close()
server.close()