import socket
import threading
import time

from Objetos.Vendas import Vendas
from Objetos.Aeroporto import Aeroporto
from Estruturas.Excecoes import AviaoException,CompraExcept
from Funcao.Compra import comprar_cadeira

Aeroporto = Aeroporto()
Aeroporto.inserir_avioes()
Vendas = Vendas()

#mutex já setado
mutex = threading.Semaphore(1)

#dados para tupla porta/ip
HOST = '0.0.0.0'
PORT = 40000 

#organização serv

print('001 OK')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(10)

def conecta_cliente(con_cli, cliente):
	print('Cliente:', cliente)
	while True:
		msg = con_cli.recv(1024)
		if not msg or not envio_dados_cliente(msg, con_cli, cliente): break
	con_cli.close()
	print('002', cliente)

def envio_dados_cliente(msg, con_cli, cliente):
	msg = msg.decode()
	print('Cliente: ', cliente, ' chamou a função', msg)
	msg = msg.split()

	if msg[0].lower() == 'obter':
		mutex.acquire()
		con_cli.send(str.encode('003'))
		try:
			if msg[1].lower() == 'voos' :
				con_cli.send(str.encode(str(Aeroporto)))
			elif msg[1].lower() == 'id' :
				con_cli.send(str.encode(Vendas.compras_realizadas()))
			else:
				con_cli.send(str.encode('104'))
		except ValueError:
			con_cli.send(str.encode('102'))
		mutex.release()
	elif msg[0].lower() == 'verificar':
		mutex.acquire()
		con_cli.send(str.encode('004'))
		try:
			if msg[1].lower()=='voo':
				con_cli.send(str.encode(Aeroporto.inspecionar_dados_voo(msg[2])))
			elif msg[1].lower()=='id':
				con_cli.send(str.encode(Vendas.verificar_compra(int(msg[2]))))
			elif msg[1].lower()=='assentos':
				dados_verificar_assento = Aeroporto.verificar_cadeiras(msg[2])
				if dados_verificar_assento is None:
					raise AviaoException('ERROR: Avião inexistente ou inválido!')
				con_cli.send(str.encode(dados_verificar_assento))
			else:
				con_cli.send(str.encode('101'))
		except ValueError:
			con_cli.send(str.encode('105'))
		except IndexError:
			con_cli.send(str.encode('106'))
		except CompraExcept:
			con_cli.send(str.encode('110'))
		except AviaoException:
			con_cli.send(str.encode('111'))
		mutex.release()
	elif msg[0].lower() == 'comprar':
		
		mutex.acquire()
		con_cli.send(str.encode('005'))
		try:
			comprar_cadeira(Aeroporto,Vendas, msg[1], int(msg[2]), msg[3])
			time.sleep(5)
			con_cli.send(str.encode('006'))	
		except CompraExcept:
			con_cli.send(str.encode('109'))
		except Exception:
			con_cli.send(str.encode('107'))	
		mutex.release()
		
	elif msg[0].lower() == 'quit':
		con_cli.send(str.encode('007'))
		return False
	else:
		con_cli.send(str.encode('Comando Inválido. Tente Novamente!\n'))
	return True


while True:
	try:
		con_cli, cliente = sock.accept()
	except: break
	threading.Thread(target=conecta_cliente, args=(con_cli, cliente)).start()

sock.close()


