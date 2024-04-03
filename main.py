# stolen from https://gist.github.com/limingzju/6483619 made to work in python 3
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print(f"Connected by {addr}")
while 1:
  data = conn.recv(1024)
  if not data: break
  conn.sendall(data)
conn.close()