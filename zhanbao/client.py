import socket
import time
import struct


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

data1 = struct.pack("i", len("hello"))
client.send(data1)
client.send("hello".encode("utf-8"))

data2 = struct.pack("i", len("world"))
client.send(data2)
client.send("world".encode("utf-8"))

