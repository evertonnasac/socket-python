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

    mensagemEncoded = str(mensagem)
    cliente.sendall((mensagemEncoded.encode("utf-8")))

    resposta = cliente.recv(1024)
    
    return resposta.decode("utf-8")

# Função que retorna o total de vendas de um vendedor escolhido pelo usuário
def getTotalVendedor(opcao):    
    print("Vendedores cadastrados:\nAna\nJoao\nJose\nMaria")
    print("Digite o nome do vendedor")
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

        
        

    

def getTotalVendasUmaLoja(opcao):
    print("Digite o código da loja")
    print("1 - LOJA 1")
    print("2 - LOJA 2")
    loja = input("") 

    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao, "loja": loja }
    retorno = eval(sendMessage(mensagem))

    loja = retorno["loja"]
    total = retorno["total"]
    print(f"Loja: {loja} --- Total de vendas: {total} ")


def getMelhorLoja(opcao):
    mensagem = {"operacao": CODIGO_OPERACAO, "opcao": opcao}
    resposta = eval(sendMessage(mensagem))

    if resposta["type"] == "string":
        print(resposta["message"])
        return 

    



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
        tese = 0
    
    elif opcao == "5":
        getMelhorVendedor(opcao)

    print("DIGITE QUALQUER LETRA PARA INICIAR A OPERAÇÃO OU DIGITE O NUMERO 0 (ZERO) PARA ENCERRAR")
    entrada = input()

print("Encerrando o cliente")
cliente.close()