import socket

print('Digite o ip ao qual deseja se conectar')
ip = input()
print('Digite a porta a qual deseja se conectar')
port = int(input())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (ip, port)
s.connect(dest)

msg_client = ''

print('------------------------------------------------------------\n' +
	  '| Digite '+ r'\UPTIME' + ' para saber o tempo de execução do servidor|\n' +
	  '| Digite ' + r'\REQNUM' + ' para saber a qte de requisições recebidas |\n' +
	  '| Digite ' + r'\CLOSE' + ' para encerrar a conexão                    |\n' +
	  '------------------------------------------------------------\n')
while True:
	msg_client = input()
	if msg_client == r'\CLOSE':
		break
	s.send(msg_client.encode())
	msg_server = s.recv(1024)
	print("Mensagem do servidor: {}".format(msg_server.decode()))
s.close()