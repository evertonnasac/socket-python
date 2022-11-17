# ------------------
# Cliente Funcionario Socket TCP
# ------------------

print("Gerente")


import socket
import datetime

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
		print("Siga as orientações abaixo para informar a data corretamente")
		
		try:

			print("Digite o dia na data a ser pesquisada ")
			dia = int((input()))

			print("Digite o numero do mes correspondente a data a ser pesquisada:\n" +

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

			print("Digite o ano por extenso (com 4 dígitos) na data a ser pesauisada. Exemplo: 2022 ou 1998")
			ano = int(input())
			
			data = datetime.date(ano, mes, dia)
			controle = False
			return data

		except: 
			print("Por favor, preencha os campos de forma correta")

# Função que retorna o total de vendas de um vendedor escolhido pelo usuário
def getTotalVendedor(opcao):    
    print("Vendedores cadastrados:\nAna\nJoao\nJose\nMaria")
    print("Digite o nome do vendedor entre os listados acima")
    nome = input()

    # Cria um dicionário com os dados e passa para a função que troca menssagens com o servidor
    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao, "vendedor": nome}
    resposta = eval(sendMessage(mensagem))

    # Verifica se a resposta é um dicionrario ou string para o tratemento adequado
    if resposta["type"] == "string":
        print(resposta["message"])
        return 
        
    nome = resposta["nome"]
    vendas = resposta["vendas"]

    print(f"Nome: {nome} --- Total de vendas: {vendas} ")

# Função que apresenta o vendedor com maior valor em vendas
# Pode retornar uma string avisando que nenhum vendedor registrou vendas
#  ou um dicionario contendo um ou mais vendedores, caso haja empate entre os valores
def getMelhorVendedor(opcao):
    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao}
    resposta = eval(sendMessage(mensagem))

    if resposta["type"] == "string":
        print(resposta["message"])
        return 
    
    # A chave "type" com valor "dict" signifia que só retornou um vendedor 
    elif resposta["type"] == "dict":

        # Nesse caso, a chave "valor" é uma string com o seguinte modelo: {"nome": "xxx", "valor":"yyy"}
        vendedor = eval(resposta["valor"])
        print(f"Nome: {vendedor['nome'].title()} --- Total em vendas: {vendedor['vendas']}")
        
    # a chave "type" com valor "list" revela que foram retornados mais de um vendedor com valores de vendas iguais
    elif resposta["type"] == "list":

        # Nesse caso, a chave "valor" é uma string com o modelo igual a condição anterior, com mais ocorrências, separadas por "*"
        # Exemplo: {"nome": "xxx", "valor":"yyy"}*{"nome": "xxx", "valor":"yyy"}....
        lista = resposta["valor"]

        # Os dados são convertidos em uma lista e em seguida, cada item são convertidos em dicionario
        lista = list(lista.split("*"))

        print("Os vendedores com maior valor em vendas são:")
        for x in range(len(lista)):
            lista[x] = eval(lista[x])
            print(f"Nome: {lista[x]['nome'].title()} --- Valor: {lista[x]['vendas']}")

def getTotalPeriodo(opcao):

    print("Informe a data INICIAL do período a ser pesquisado")
    dataInicial = getData()
    print("Informe a data FINAL do período a ser pesquisado")
    dataFinal = getData()

    print("END")

    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao, "inicial": dataInicial, "final": dataFinal}
    retorno =  sendMessage(mensagem)
    print(retorno)




def getTotalVendasUmaLoja(opcao):
    print("Digite o código da loja")
    print("1 - LOJA 1")
    print("2 - LOJA 2")
    loja = input("") 

    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao, "loja": loja }
    retorno = eval(sendMessage(mensagem))

    if retorno["type"] == "string":
        print(retorno["message"])
        return

    print(f"Loja: {retorno['loja']} --- Total de vendas: {retorno['total']} ")


def getMelhorLoja(opcao):
    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao}
    resposta = eval(sendMessage(mensagem))

    if resposta["type"] == "string":
        print(resposta["message"])
        return 

    # A chave "type" com valor "dict" signifia que só retornou uma loja
    elif resposta["type"] == "dict":

        # Nesse caso, a chave "valor" é uma string com o seguinte modelo: {"loja": "xxx", "total":"yyy"}
        loja = eval(resposta["valor"])
        
        print(f"Nome: {loja['loja'].title()} --- Total em vendas: {loja['total']}")
        
    # a chave "type" com valor "list" revela que foram retornados mais de uma loja com valores de vendas iguais
    elif resposta["type"] == "list":

        # Nesse caso, a chave "valor" é uma string com o modelo igual a condição anterior, com mais ocorrências, separadas por "*"
        # Exemplo: {"loja": "xxx", "total":"yyy"}*{"loja": "xxx", "total":"yyy"}....
        lista = resposta["valor"]

        # Os dados são convertidos em uma lista e em seguida, cada item são convertidos em dicionario
        lista = list(lista.split("*"))

        print("As lojas com maior valor em vendas são:")
        for x in range(len(lista)):
            lista[x] = eval(lista[x])
            print(f"Nome: {lista[x]['loja'].title()} --- Valor: {lista[x]['total']}")


#...........................Menu de opções.......................

print("DIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR")
entrada = input()

while entrada != "0":
    print("Escolha uma das opções abaixo digitando o numero correspondente a operação desejada")
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

    print("DIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR")
    entrada = input()

print("Encerrando o cliente")
cliente.close()