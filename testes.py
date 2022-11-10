funcionarios = [
	{"nome": "joao", "vendas" : 25, "unidade" : 1},
	{"nome": "ana", "vendas" : 5, "unidade" : 2},
	{"nome": "jose", "vendas" : 15, "unidade" : 1},
	{"nome": "maria", "vendas" : 25, "unidade" : 2},
]

gerentes = [
	{"nome" : "bento", "unidade": 1 },
    {"nome" : "paula", "unidade": 2 }
]

unidade_1 = [

    17500, 
    25000, 
    17500,
    18500, 
    17950,
    26758,
    15000, 
    25000, 
    17500,
    18500, 
    0,
    0
]

unidade_2 = [

    17500, 
    25000, 
    17500,
    18500, 
    17950,
    26758,
    15000, 
    25000, 
    17500,
    18500, 
    0,
    0
]

# Registra venda pelo vendedor
def registrarVenda(funcionario, valor): 
    for func in funcionarios:
        if func["nome"] == funcionario:
            registro = funcionarios[funcionarios.index(func)]
            registro["vendas"] += valor
            unidade = registro["unidade"]
            atualizarUnidade(unidade, valor, 10)



# Atualiza o total de vendas quando o vendedor registrar venda
def atualizarUnidade(unidade, valor, mesAtual):
    if unidade == 1:
        unidade_1[mesAtual] += valor

    elif unidade == 2:
        unidade_2[mesAtual] += valor

#registrarVenda("jose", 200)

# Retorna a idenficação da loja que mais vendeu
def getLojaMaior ():
    total_loja_1 = calculaTotalLoja(unidade_1)
    total_loja_2 = calculaTotalLoja(unidade_2)
    if total_loja_1 > total_loja_2:
        return "Loja 1"
    
    else:
        return "Loja 2"

# Calcula o total de vendas de uma loja
def calculaTotalLoja (unidade):
    total = 0
    for valor in unidade:
        total += valor

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



def calcularPeriodoPorLoja(inicio, fim, loja):
    total = 0
    if loja == "1" :
        total = calcularVendasPeriodo(inicio, fim, unidade_1)
    
    elif loja == "2":
        total = calcularPeriodoPorLoja(inicio, fim, unidade_2)

    return total



def calcularVendasPeriodo(inicio, fim, loja):
    total = -1
    for indice in range(inicio, fim + 1):
        total += loja[indice]
    
    return total

print(calcularPeriodoPorLoja(1, 2, "1"))
