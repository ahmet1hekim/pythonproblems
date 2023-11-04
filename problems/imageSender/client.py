import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',1025))

f=open("/home/alex/Documents/problems/imageSender/toSend.jpg","rb")
parca = f.read(1024)

while parca:
    client.send(parca)
    parca = f.read(1024)


f.close()
client.close()
