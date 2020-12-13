import socket
s = socket.socket()
host = input(str("please enter host address of sender: "))
port = 8080
s.connect(('192.168.56.105',port))
print("connected ...")

filename = input(str("enter filename from sender:"))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("file received from sender")
s.close()

