
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


loja_1 = [
    {"valor": 200.00, "data": datetime.date(2022,10,20)},
    {"valor": 100.00, "data": datetime.date(2022,7,20)},
    {"valor": 400.00, "data": datetime.date(2022,9,20)}
]

loja_2 = [
    {"valor": 300.00, "data": datetime.date(2022,11,20)},
    {"valor": 50.00, "data": datetime.date(2022,6,20)},
    {"valor": 400.00, "data": datetime.date(2022,5,20)}
]



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
        return {"type":"string", "message": "Nenhuma loja tem venda registrada"}

    # Trazendo o somatório do valor de vendas de cada lista de lojas
    loja1 = calculaTotalLoja(loja_1, "Loja_1")
    loja2 = calculaTotalLoja(loja_2, "Loja_2")

    # Filtrando somente  os dados necessários e adicionando na lista total
    loja1 = {"loja": loja1["loja"], "total": loja1["total"]}
    total.append(loja1)

    loja2 = {"loja": loja2["loja"], "total": loja2["total"]}
    total.append(loja2)

    # Iniciando a verificação de qual loja tem o maior valor total
    valor = 0.0
    melhorLoja = []

    for item in total :

        if item["total"] <= 0.0:
            continue

        if item["total"] > valor:
            valor = item["total"]
            melhorLoja.clear()
            melhorLoja.append(str(item))
        
        elif item["total"] == valor:
            melhorLoja.append(str(item))

    if len(melhorLoja) == 0:
        return {"type": "string", "message" :"Nenhuma loja tem venda registrada"}

    elif len(melhorLoja) == 1:
        return {"type": "dict", "valor": melhorLoja[0]}

    return {"type": "list", "valor": "*".join(melhorLoja)}


    #ordem = sorted(total, key = lambda row: row["valor"], reverse=1)
    #return ordem[0]


# Calcula o total de vendas de uma loja
def calculaTotalLoja (array, descricao):
    total = 0.0
    if len(array) > 0:
        for registro in array:
            total += registro["valor"] 

    return {"type":"dict", "loja": descricao, "total": total}


#Calcula o total de vendas da rede por periodo
def calculaPeriodo(inicial, final):

    #Cria uma lista com todos os registros das  listas correspondente a cada loja
    totalVendas = loja_1 + loja_2
    
    # Ordena os registros de venda por maior data
    totalVendas = sorted(totalVendas, key = lambda row: row["data"])

    indiceInical =-1
    indiceFinal = len(totalVendas)

    # busca o indice inical para percorrer a lista "totalVendas" 
    for venda in totalVendas:
        if venda["data"] >= inicial:
            indiceInical = totalVendas.index(venda)
            break

    if indiceInical < 0:
        return "Não existe vendas realizadas a partir da data inicial informada"

    # Busca o indice final para percorrer a lista "totalVendas"    
    for venda in range(indiceInical, len(totalVendas)):
        if totalVendas[venda]["data"] > final:
            indiceFinal = venda
            break

    # Realiza a soma do valor das vendas na lista "totalVendas" 
    #  a partir do indice inicial e final encontrados
    valorTotal = 0.0
    for venda in range(indiceInical, indiceFinal):
        valorTotal += totalVendas[venda]["valor"]
    
    print(valorTotal)

    return f"O Valor total de vendas no período de {inicial} a {final} é de {valorTotal}"


# Retorna o (os) vendor(es) com maior numero de vendas
def getMelhorVendedor ():
    vendedor = []
    valor = 0.0

    for func in vendedores:
        if func["vendas"] <= 0.0:
            continue
        
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



# Retorna o valor total de vendas do vendedor requerido
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
                retorno = {"type": "string", "message" : "ERROR: Loja não encontrada"}
        
        elif dados["opcao"] == "4":
            retorno = calculaPeriodo(dados["inicial"], dados["final"])

        elif dados["opcao"] == "5":
            retorno = getMelhorLoja()
        
    retorno = str(retorno)    
        
    conexaoCliente.sendall(retorno.encode("utf-8"))

# mensagem de encerramento
print("Servidor encerrado.")