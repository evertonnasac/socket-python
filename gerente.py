# ------------------
# Cliente Funcionario Socket TCP
# ------------------


print("GERENTE")


import socket
import datetime
import os

# definindo ip e porta
HOST = '127.0.0.15'       
PORT = 9000              
CODIGO_OPERACAO = "2"

# criando o socket
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# cliente se conectando ao servidor
cliente.connect((HOST,PORT))

# Realiza a troca de mensagens com o servidor
def sendMessage(mensagem):

    mensagemStr = str(mensagem)
    cliente.sendall((mensagemStr.encode("utf-8")))

    resposta = cliente.recv(1024)
    
    return resposta.decode("utf-8")



def getData():
	controle = True

	while controle:
		print("\nSiga as orientações abaixo para informar a data corretamente:\n")
		
		try:

			print("\nDigite o dia na data a ser pesquisada: \n ")
			dia = int((input()))

			print("\nDigite o numero do mes correspondente a data a ser pesquisada:\n" +

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

			print("\nDigite o ano por extenso (com 4 dígitos) na data a ser pesauisada. Exemplo: 2022 ou 1998\n")
			ano = int(input())
			
			data = datetime.date(ano, mes, dia)
			controle = False
			return data

		except: 
			print("\nPor favor, preencha os campos de forma correta\n")

# Função que retorna o total de vendas de um vendedor escolhido pelo usuário
def getTotalVendedor(opcao):    
    print("\nVendedores cadastrados:\nAna\nJoao\nJose\nMaria\n")
    print("Digite o nome do vendedor entre os listados acima\n")
    nome = input()

    # Cria um dicionário com os dados e passa para a função que troca menssagens com o servidor
    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao, "vendedor": nome}
    print("\n")
    resposta = eval(sendMessage(mensagem))

    # Verifica se a resposta é um dicionrario ou string para o tratemento adequado
    if resposta["type"] == "string":
        print("\n")
        print(resposta["message"])
        return 
        
    nome = resposta["nome"]
    vendas = resposta["vendas"]

    print("\n")
    print(f"Nome: {nome} --- Total de vendas: {vendas} ")

# Função que apresenta o vendedor com maior valor em vendas
# Pode retornar uma string avisando que nenhum vendedor registrou vendas
#  ou um dicionario contendo um ou mais vendedores, caso haja empate entre os valores
def getMelhorVendedor(opcao):
    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao}
    resposta = eval(sendMessage(mensagem))

    if resposta["type"] == "string":
        print("\n")
        print(resposta["message"])
        return 
    
    # A chave "type" com valor "dict" signifia que só retornou um vendedor 
    elif resposta["type"] == "dict":

        # Nesse caso, a chave "valor" é uma string com o seguinte modelo: {"nome": "xxx", "valor":"yyy"}
        vendedor = eval(resposta["valor"])
        print("\n")
        print(f"Nome: {vendedor['nome'].title()} --- Total em vendas: {vendedor['vendas']}")
        
    # a chave "type" com valor "list" revela que foram retornados mais de um vendedor com valores de vendas iguais
    elif resposta["type"] == "list":

        # Nesse caso, a chave "valor" é uma string com o modelo igual a condição anterior, com mais ocorrências, separadas por "*"
        # Exemplo: {"nome": "xxx", "valor":"yyy"}*{"nome": "xxx", "valor":"yyy"}....
        lista = resposta["valor"]

        # Os dados são convertidos em uma lista e em seguida, cada item são convertidos em dicionario
        lista = list(lista.split("*"))

        print("\nOs vendedores com maior valor em vendas são:\n")
        for x in range(len(lista)):
            lista[x] = eval(lista[x])
            print(f"Nome: {lista[x]['nome'].title()} --- Valor: {lista[x]['vendas']}")
            print("\n")

# Solicita ao usuario uma data inicial e uma data final, e retorna o valor total de vendas dentro do periodo
def getTotalPeriodo(opcao):

    print("\nInforme a data INICIAL do período a ser pesquisado\n")
    dataInicial = getData()
    print("\nInforme a data FINAL do período a ser pesquisado\n")
    dataFinal = getData()

    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao, "inicial": dataInicial, "final": dataFinal}
    retorno =  sendMessage(mensagem)
    print("\n")
    print(retorno)




def getTotalVendasUmaLoja(opcao):
    print("\nDigite o código da loja:\n")
    print("1 - LOJA 1")
    print("2 - LOJA 2")
    loja = input("") 

    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao, "loja": loja }
    retorno = eval(sendMessage(mensagem))

    if retorno["type"] == "string":
        print("\n")
        print(retorno["message"])
        return

    print("\n")
    print(f"Loja: {retorno['loja']} --- Total de vendas: {retorno['total']} ")


def getMelhorLoja(opcao):
    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao}
    resposta = eval(sendMessage(mensagem))

    if resposta["type"] == "string":
        print("\n")
        print(resposta["message"])
        return 

    # A chave "type" com valor "dict" signifia que só retornou uma loja
    elif resposta["type"] == "dict":

        # Nesse caso, a chave "valor" é uma string com o seguinte modelo: {"loja": "xxx", "total":"yyy"}
        loja = eval(resposta["valor"])
        
        print("\n")
        print(f"Nome: {loja['loja'].title()} --- Total em vendas: {loja['total']}")
        
    # a chave "type" com valor "list" revela que foram retornados mais de uma loja com valores de vendas iguais
    elif resposta["type"] == "list":

        # Nesse caso, a chave "valor" é uma string com o modelo igual a condição anterior, com mais ocorrências, separadas por "*"
        # Exemplo: {"loja": "xxx", "total":"yyy"}*{"loja": "xxx", "total":"yyy"}....
        lista = resposta["valor"]

        # Os dados são convertidos em uma lista e em seguida, cada item são convertidos em dicionario
        lista = list(lista.split("*"))

        print("\n")
        print("As lojas com maior valor em vendas são:\n")
        for x in range(len(lista)):
            lista[x] = eval(lista[x])
            print(f"Nome: {lista[x]['loja'].title()} --- Valor: {lista[x]['total']}")


#...........................Menu de opções.......................

print("\nDIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR\n")
entrada = input()
os.system('clear') or None

while entrada != "0":
    print("\nEscolha uma das opções abaixo digitando o numero correspondente a operação desejada:\n")
    print("1 - Valor total de vendas de um vendedor \n"+
          "2 - Vendedor com maior valor acumulado em vendas\n"+
          "3 - Valor total de vendas de uma loja\n"+
          "4 - valor total de vendas da rede de lojas por um período\n"+
          "5 - Loja com maior com maior valor acumulado em vendas")

    opcao = input()

    if opcao == "1":
        getTotalVendedor(opcao)

    elif opcao == "2":
        getMelhorVendedor(opcao)

    elif opcao == "3":
        getTotalVendasUmaLoja(opcao)

    elif opcao == "4":
        getTotalPeriodo(opcao)
    
    elif opcao == "5":
        getMelhorLoja(opcao)

    print("\nDIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR\n")
    entrada = input()
    os.system('clear') or None

print("Encerrando o GERENTE")
cliente.close()