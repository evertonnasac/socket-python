
# importando a biblioteca
import socket


#............................Funções...................
vendedores = [
	{"nome": "joao", "vendas" : 0, "unidade" : 0},
	{"nome": "ana", "vendas" : 0, "unidade" : 0},
	{"nome": "jose", "vendas" : 0, "unidade" : 0},
	{"nome": "maria", "vendas" : 0, "unidade" : 0},
]

gerentes = [
	{"nome" : "bento", "unidade": 1 },
    {"nome" : "paula", "unidade": 2 }
]


loja_1 = []

loja_2 = []

#...................Funções.....................

# Registra venda pelo vendedor
def registrarVenda(venda): 

    for vend in vendedores:
        if vend["nome"] == venda["funcionario"]:
            registro = vendedores[vendedores.index(vend)]
            registro["vendas"] += venda["valor"]

            if venda["loja"] == "1":
                loja_1.append(venda)
            
            elif venda["loja"] == "2":
                loja_2.append(venda)

            return "Operação Realizada"

        else:
            return "Vendedor não encontrado"
			

# Retorna a idenficação da loja que mais vendeu
def getLojaMaior ():
    total_loja_1 = calculaTotalLoja(loja_1)
    total_loja_2 = calculaTotalLoja(loja_2)

    if total_loja_1 > total_loja_2:
        return "Loja 1"
    
    else:
        return "Loja 2"

# Calcula o total de vendas de uma loja
def calculaTotalLoja (unidade):
    total = 0
    if len(unidade) > 0:
        for registro in unidade:
            total += registro["valor"] 

    return total

# Retorna o (os) vendor com maior numero de vendas
def getMaiorVendedor ():
    vendedor = []
    valor = -1

    for func in funcionarios:
        if func["vendas"] > valor:
            valor = func["vendas"]
            vendedor.clear()
            vendedor.append(func)
        
        elif func["vendas"] == valor:
            vendedor.append(func)

    return vendedor


# definindo ip e porta
HOST = '127.0.0.15'     
PORT = 9000              

# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind((HOST,PORT))

# servidor escutando (aguardando cliente)
servidor.listen()
print("Aguardando cliente...")


# cliente conectou - recuperando informações do cliente
conexaoCliente, enderecoCliente = servidor.accept()
print(f"Cliente {enderecoCliente} conectou.")


# conversando com o cliente
while (True):
	# recebendo dados
	receive = conexaoCliente.recv(1024)
	# testando dados enviados

	if (not receive):
		# encerrando conexão e saindo do loop
		print ("Encerrando a conexão...")
		conexaoCliente.close()
		break

	mensagem = receive.decode("utf-8")
	dados = eval(mensagem)
    codigo_operacao = dados["operacao"]

    if (codigo_operacao == "1"):
        retorno = registrarVenda(mensagem)
        conexaoCliente.sendall(retorno.encode("utf-8"))

# mensagem de encerramento
print("Servidor encerrado.")