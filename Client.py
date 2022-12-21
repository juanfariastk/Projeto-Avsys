import socket
import sys

#tupla ip/porta
HOST = 'localhost' 
PORT = 40000


#Dicionário de comandos
def metodos_suportados(comando_atual):
	comandos_suportados = {
		'sair': 'quit',
		'comprar' : 'comprar',
		'obter' : 'obter',
		'verificar': 'verificar',
	}
	comando = comando_atual.split()
	if comando[0].lower() in comandos_suportados:
		comando[0] = comandos_suportados[comando[0].lower()]
		return " ".join(comando)
	else:
		return False
		
if len(sys.argv) > 1:
	HOST = sys.argv[1]

print('Servidor:', HOST+':'+str(PORT))

#Implementação do Socket TCP
serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)

print('Para encerrar use SAIR \n')


#Print da interface no terminal
while True:
	print('''
               ╔═══════════════════════════╗
               ║ ╔═══════════════════════╗ ║
               ║ ║                       ║ ║
               ║ ║      ► Obter          ║ ║
               ║ ║      ► Verificar      ║ ║
               ║ ║      ► Comprar        ║ ║
               ║ ║                       ║ ║
               ║ ║                       ║ ║
               ║ ╚═══════════════════════╝ ║
               ╚═══════════════════════════╝
           ╔═════\_____     []     _______/══════╗
          /           /____________\             ║
         ╔═══════════════════════════════════╗   ║ 
         ║                                   ║   ║
         ║  _ _ _                 [-------]  ║   ║   
         ║  o o o                 [-------]  ║  /    
         ╚═══════════════════════════════════╝/     
   ''')
	
	try:
		comando = input('Digite um comando ')
	except:
		comando = 'SAIR'
	comando_atual = metodos_suportados(comando)
	if not comando_atual:
		print('Comando indefinido:', comando)
	else:
		sock.send(str.encode(comando_atual))
		dados = sock.recv(1024)

		if not dados: break

		msg_status = dados.decode().split('\n')[0]
		dados = dados[len(msg_status)+1:]
		
		if msg_status == '003':
			print('Comando OBTER chamado com sucesso!')
		elif msg_status == '004':
			print('Comando VERIFICAR chamado com sucesso!')
		elif msg_status == '005':
			print('Comando COMPRAR chamado com sucesso')
		elif msg_status == '007':
			print('Saindo do servidor...')

		comando_atual = comando_atual.split()
		comando_atual[0] = comando_atual[0].lower()

		if comando_atual[0].lower() == 'quit':
			break
		elif comando_atual[0].lower() == 'obter':
			print('Voos disponíveis:')
			print('''

 __  _
 \ `/ |
  \__`!
  / ,' `-._________________
 '-'\_____               |_|`-.
    <____()-=O=O=O=O=O=[]====--)
      `.___ ,-----,_______...-'
           /    .'
          /   .'
         /  .'         
         `-'

 ''')
			print("  Voo 1", "  Voo 2", "  Voo 3", "  Voo 4", "  Voo 5")
			dados = sock.recv(1024)
			if dados.decode()=='104':
				print('Erro! Argumento Inválido!')
			elif dados.decode()=='102':
				print('Erro! Digite dados válidos!')
			else:
				print(dados.decode())
		elif comando_atual[0].lower() == 'verificar':
			dados = sock.recv(1024)
			if dados.decode() == '103':
				print('ERROR! Avião inexistente ou inválido!')
			elif dados.decode() == '101':
				print('Erro!!! Digite o comando corretamente!')
			elif dados.decode() == '105':
				print('Digite dados válidos para realizar a verificação!')
			elif dados.decode() == '106':
				print('Faltou o Tipo ou ID para realizar a verificação!')
			elif dados.decode() == '110':
				print('ERROR! Este ID de compra não existe!')
			elif dados.decode() == '111':
				print('ERROR! Este ID do Avião é inválido!')
			else:
				print(dados.decode())

		elif comando_atual[0].lower() == 'comprar':
			dados = sock.recv(1024)
			if dados.decode() == '006':
				print('Assento comprado com Sucesso!')
			elif dados.decode() == '109':
				print('ERRO! Este assento já foi comprado!\nEscolha um outro assento.')
			elif dados.decode() == '107':
				print('ERRO! Complete os parâmetros do comando corretamente e tente novamente.')
			else:
				print(dados)
		
sock.close() #Encerramento do SOCKET
