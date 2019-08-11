import socket
print('Digite o ip ao qual deseja se conectar')
ip = input()
print('Digite a porta a qual deseja se conectar')
port = int(input())
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (ip, port)

print('------------------------------------------------------------\n' +
    '| Digite '+ r'\UPTIME' + ' para saber o tempo de execução do servidor|\n' +
    '| Digite ' + r'\REQNUM' + ' para saber a qte de requisições recebidas |\n' +
    '| Digite ' + r'\CLOSE' + ' para encerrar a conexão                    |\n' +
    '------------------------------------------------------------\n')

msg_client = ''
while True:
  msg_client = input()
  if msg_client == r'\CLOSE':
    break
  udp.sendto(msg_client.encode(), dest)
  msg_server = udp.recvfrom(1024)
  print("Mensagem do servidor: {}".format(msg_server[0].decode()))
udp.close()