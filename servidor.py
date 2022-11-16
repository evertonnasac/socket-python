
# importando a biblioteca
import socket
import datetime

#............................Dados...................
vendedores = [
	{"nome": "joao", "vendas" : 10.0},
	{"nome": "ana", "vendas" : 500.0},
	{"nome": "jose", "vendas" : 500.0},
	{"nome": "maria", "vendas" : 500.0}
]


loja_1 = []

loja_2 = []



#...................Funções.....................

# Registra venda pelo vendedor
def registrarVenda(venda): 

    for vendedor in vendedores:
   
        if vendedor["nome"] == venda["vendedor"]:
            registro = vendedores[vendedores.index(vendedor)]
            registro["vendas"] += float(venda["valor"])

            novaVenda = {"valor": float(venda["valor"]), "data":venda["data"]}

            if venda["loja"] == "1":
                loja_1.append(novaVenda)
            
            elif venda["loja"] == "2":
                loja_2.append(novaVenda)

            return "Operação realizada com sucesso"
    
    return "ERRO: Operção não realizada"

    
		
# Retorna a idenficação da loja que mais vendeu
def getMelhorLoja ():
    total = []

    if len(loja_1) == 0 and len(loja_2) == 0 :
        return {"type":"string", "message": "Nenhuma loja registrou venda"}

    total.append(calculaTotalLoja(loja_1, "Loja_1"))
    total.append(calculaTotalLoja(loja_2, "Loja_2"))

    ordem = sorted(total, key = lambda row: row["valor"], reverse=1)
    return ordem[0]


# Calcula o total de vendas de uma loja
def calculaTotalLoja (array, descricao):
    total = 0.0
    if len(array) > 0:
        for registro in array:
            total += registro["valor"] 

    return {"type":"dict", "loja": descricao, "total": total}


# Retorna o (os) vendor com maior numero de vendas
def getMelhorVendedor ():
    vendedor = []
    valor = 0.0

    for func in vendedores:
        if func["vendas"] > valor:
            valor = func["vendas"]
            vendedor.clear()
            vendedor.append(str(func))
        
        elif func["vendas"] == valor:
            vendedor.append(str(func))

    if valor <= 0.0:
        return {"type": "string", "message" :"Nenhum vendedor registrou venda"}

    if len(vendedor) == 1:
        return{"type": "dict", "valor": vendedor[0]}
  
    return {"type": "list", "valor": "*".join(vendedor)}



# Retorna o valor total de vendas do vendor requerido
def getTotalVendedor(vendedor):
    for func in vendedores:
        if func["nome"] == vendedor:
            return {"type": "dict", "nome": vendedor.title(), "vendas": func["vendas"]}

    return {"type": "string" , "message":"Vendedor nao encontrado"}


#.............................Conexao.........................

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

    dados = eval(receive.decode("utf-8"))
    codigo_operacao = dados["operacao"]
    retorno = ""

    if codigo_operacao == "1":
        retorno = registrarVenda(dados)

    elif codigo_operacao == "2":
        if dados["opcao"] =="1":
            retorno = getTotalVendedor(dados["vendedor"])

        elif dados["opcao"] == "2":
            retorno = getMelhorVendedor()

        elif dados["opcao"] == "3":
            
            if dados["loja"] == "1":
                retorno = calculaTotalLoja(loja_1, "Loja 1")
            elif dados["loja"] == "2":
                retorno = calculaTotalLoja(loja_2, "Loja 2")
            else:
                retorno = " ERROR: Loja não encontrada"
        
        elif dados["opcao"] == "4":
            retorno = "Error 404 not found"

        elif dados["opcao"] == "5":
            retorno = getMelhorLoja()
        
    retorno = str(retorno)    
        
    conexaoCliente.sendall(retorno.encode("utf-8"))

# mensagem de encerramento
print("Servidor encerrado.")