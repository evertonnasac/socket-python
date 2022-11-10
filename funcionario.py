# ------------------
# Cliente Funcionario Socket TCP
# ------------------

print("Vendedor")

# importando a biblioteca
import socket

# definindo ip e porta
HOST = '127.0.0.15'       # Substituir pelo endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando

CODIGO_OPERACAO = "1"

# criando o socket
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# cliente se conectando ao servidor
cliente.connect((HOST,PORT))

def getDadosUsuario():

	print("Vendedores cadastrados:\nAna\nJoao\nJose\nMaria")
	print("Digite o nome do vendedor cadastrado entre os listados acima")
	vendedor = input()
	vendedor = vendedor.lower()

	print("Digite o numero do mes correspondente valor da venda realizada:\n" +

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
	data = input()

	print("Digite o código da loja")
	print("1 - LOJA 1")
	print("2 - LOJA 2")
	loja = input("") 

	print("Digite o valor da venda realizada")
	valor = input("") 

	return  str({"operacao": CODIGO_OPERACAO, 
				"vendedor": vendedor, 
				"data": data, 
				"valor": valor,
				"loja": loja})
	


print("DIGITE QUALQUER LETRA PARA INICIAR A OṔERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR")
entrada = input()

if entrada != 0:
	mensgeagem = getDadosUsuario()

while (entrada != 0):

	# Enviando mensagem ao servidor
	cliente.sendall(mensagem.encode("utf-8"))

	# Recebendo resposta do servidor
	resposta = cliente.recv(1024)

	# exibindo resposta
	print("... >>> RESPOSTA DA OPERAÇÃO: ", resposta.decode("utf-8"))
    
	# Obtendo nova mensagem do usuário
	print("DIGITE QUALQUER LETRA PARA INICIAR A OṔERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR")
	mensagem = input()

	if mensagem != 0:
		mensagem = getDadosUsuario()
		

print("Encerrando o cliente")
cliente.close()