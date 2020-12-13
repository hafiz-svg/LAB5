import socket
import os

port = 8080
s = socket.socket()
host = socket.gethostname()
s.bind(('', port))
s.listen(1)
print(host)
print ('Server listening....')
conn, addr = s.accept()
print (addr, 'Got connection from sender')
filename= input(str("please filename to send: "))
file = open(filename , 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("file been send")
s.close()
