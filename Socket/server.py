import socket
from datetime import datetime

ip = '127.0.0.1'
port = 5004

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (ip, port)
s.bind(orig)
s.listen(1)
conn, addr = s.accept()

start = datetime.now()
reqnum = 0

while True:
	msg = conn.recv(1024)
	print("Mensagem do cliente: {}".format(msg.decode()))
	if not msg.decode(): break
	if msg.decode() == r'\UPTIME':
		reqnum = reqnum + 1
		now = datetime.now() - start
		conn.send(str(now).encode())
	if msg.decode() == r'\REQNUM':
		reqnum = reqnum + 1
		conn.send(str(reqnum).encode())
conn.close()