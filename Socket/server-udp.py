import socket
from datetime import datetime
ip = '127.0.0.1'           
port = 5000            
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (ip, port)
udp.bind(orig)

start = datetime.now()
reqnum = 0

while True:
	msg, address = udp.recvfrom(1024)
	print("Mensagem do cliente: {}".format(msg.decode()))
	if msg.decode() == r'\UPTIME':
		reqnum = reqnum + 1
		now = datetime.now() - start
		udp.sendto(str(now).encode(), address)
	if msg.decode() == r'\REQNUM':
		reqnum = reqnum + 1
		udp.sendto(str(reqnum).encode(), address)