# ------------------
# Cliente Vendedor Socket TCP
# ------------------

import os

print("VENDEDOR")


import socket
import datetime

# definindo ip e porta
HOST = '127.0.0.15'       
PORT = 9000              
CODIGO_OPERACAO = "1"

# criando o socket
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# cliente se conectando ao servidor
cliente.connect((HOST,PORT))

def getValorVenda():
	controle = True

	while controle:
		try:
			print("\nDigite o valor da venda realizada. Exemplo: 19.90\n")
			valor = float(input())
			controle = False
			return valor

		except:
			print("\nPor fvor, digite o valor da venda conforme as orientações anteriores\n")
			controle = True


def getDataVenda():
	controle = True

	while controle:
		print("\nSiga as orientações abaixo para registrar a data da venda:\n")

		print("\nDigite o dia da venda realizada\n")
		dia = int((input()))
		
		try:
			print("\nDigite o numero do mes correspondente da venda realizada:\n" +

				"1 -  JANEIRO\n" +
				"2 -  FEVEREIRO\n" +
				"3 -  MARÇO\n" +
				"4 -  ABRIL\n" +
				"5 -  MAIO\n" +
				"6 -  JUNHO\n" +
				"7 -  JULHO\n" +
				"8 -  AGOSTO\n" +
				"9 -  SETEMBRO\n" +
				"10 - OUTUBRO\n" +
				"11 - NOVEMBRO\n" +
				"12 - DEZEMBRO\n" 
			)
			mes = int(input())

			print("\nDigite o ano por extenso (com 4 dígitos) da venda realizada. Exemplo: 2022 ou 1998\n")
			ano = int(input())

			
			data = datetime.date(ano, mes, dia)
			controle = False
			return data

		except: 
			print("\nPor favor, preencha os valores para data de forma correta\n")



def getDadosUsuario():
	os.system('clear') or None
	print("Vendedores cadastrados:\nAna\nJoao\nJose\nMaria")
	print("\nDigite o nome do vendedor cadastrado entre os listados acima")
	vendedor = input()
	vendedor = vendedor.lower()

	data = getDataVenda()

	print("\nDigite o código da loja")
	print("1 - LOJA 1")
	print("2 - LOJA 2")
	loja = input("") 

	valor = str(getValorVenda())

	return  str({"operacao": CODIGO_OPERACAO, 
				"vendedor": vendedor, 
				"data": data, 
				"valor": valor,
				"loja": loja})
	


print("\nDIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR\n")
entrada = input()

while (entrada != "0"):

	mensagem = getDadosUsuario()

	# Enviando mensagem ao servidor
	cliente.sendall(mensagem.encode("utf-8"))

	# Recebendo resposta do servidor
	resposta = cliente.recv(1024)

	# exibindo resposta
	print("\n")
	print(resposta.decode("utf-8"))
    
	# Obtendo nova mensagem do usuário
	print("\nDIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR\n")
	entrada = input()
	os.system('clear') or None
		

print("Encerrando o VENDEDOR")
cliente.close()