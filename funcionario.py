# ------------------
# Cliente Funcionario Socket TCP
# ------------------

print("Vendedor")


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
			print("Digite o valor da venda realizada. Exemplo: 19.90")
			valor = float(input())
			controle = False
			return valor

		except:
			print("Por fvor, digite o valor da venda conforme as orientações anteriores")
			controle = True


def getDataVenda():
	controle = True

	while controle:
		print("Siga as orientações abaixo para registrar a data da venda")
		
		try:
			print("Digite o numero do mes correspondente da venda realizada:\n" +

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

			print("Digite o dia da venda realizada")
			dia = int((input()))

			print("Digite o ano por extenso (com 4 dígitos) da venda realizada. Exemplo: 2022 ou 1998")
			ano = int(input())

			
			data = datetime.date(ano, mes, dia)
			controle = False
			return data

		except: 
			print("Por favor, preencha os valores para data de forma correta")



def getDadosUsuario():

	print("Vendedores cadastrados:\nAna\nJoao\nJose\nMaria")
	print("Digite o nome do vendedor cadastrado entre os listados acima")
	vendedor = input()
	vendedor = vendedor.lower()

	data = getDataVenda()

	print("Digite o código da loja")
	print("1 - LOJA 1")
	print("2 - LOJA 2")
	loja = input("") 

	valor = str(getValorVenda())

	return  str({"operacao": CODIGO_OPERACAO, 
				"vendedor": vendedor, 
				"data": data, 
				"valor": valor,
				"loja": loja})
	


print("DIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR")
entrada = input()

while (entrada != "0"):

	mensagem = getDadosUsuario()

	print(mensagem)

	# Enviando mensagem ao servidor
	cliente.sendall(mensagem.encode("utf-8"))

	# Recebendo resposta do servidor
	resposta = cliente.recv(1024)

	# exibindo resposta
	print("... >>> RESPOSTA DA OPERAÇÃO: ", resposta.decode("utf-8"))
    
	# Obtendo nova mensagem do usuário
	print("DIGITE QUALQUER LETRA PARA INICIAR A OṔERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR")
	entrada = input()
		

print("Encerrando o cliente")
cliente.close()