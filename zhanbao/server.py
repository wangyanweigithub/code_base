import socket
import time
import struct


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8888))
server.listen(5)


conn, addr = server.accept()
print('connect by ', addr)
time.sleep(1)

#header = conn.recv(4)
#size = struct.unpack("i", header)[0]
#print('size', size)
#res1 = conn.recv(size)
#print('第一次 ', res1)
#
#header = conn.recv(4)
#size = struct.unpack("i", header)[0]
#print('size', size)
#res2 = conn.recv(10)
#print('第二次 ', res2)
data = conn.recv(100)
print(data)
