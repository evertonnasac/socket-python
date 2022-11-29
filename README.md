# Trabalho da UC Sistemas Distribuídos, 2022.2 - UNIFACS

## TEMA: Utilização de sockets para comunicação entre processos

## Equipe:
* Everton Nazaré do Sacramento - RA: 1272119075
* Manuelle Reis - RA: 1272116405    
* Leonardo Oliveira - RA: 1272121620
* Rafael Lima - RA: 1272117553
* Ygor Pinto Gama - RA: 1272121369

## Requisitos funcionais:
### O aplicativo deve funcionar da seguinte maneira:
* Há dois tipos de clientes: os vendedores e os gerentes.
* Vendedores informam ao sistema o valor de cada venda feita por eles.
* Gerentes consultam as informações de vendas registradas.
* O servidor hospeda as informações fornecidas por vendedores e responde
consultas dos gerentes. 

## Detalhamento do funcionamento da aplicação:
* Cliente (Vendedor)
1. Envia ao servidor uma mensagem informando uma venda realizada.
2. A mensagem deve conter um código de operação, o nome do vendedor, a
identificação da loja, a data da venda e o valor vendido.
* Cliente (Gerente)
1. Envia ao servidor uma mensagem solicitando uma das possíveis consultas:
2. Total de vendas de um vendedor (deve informar o nome do vendedor na
mensagem)
3. Total de vendas de uma loja (deve informar a identificação da loja na
mensagem)
4. Total de vendas da rede de lojas em um período (deve informar a data inicial e a
data final do período desejado)
5. Melhor vendedor (aquele que tem o maior valor acumulado de vendas)
6. Melhor loja (aquela que tem o maior valor acumulado de vendas)
7. As mensagens sempre devem conter um código de operação e os dados
necessários para a operação ser realizada.
* Servidor
1. Aguarda solicitações de clientes (escuta).
2. Recebe solicitação e identifica o tipo a partir do código de operação enviado:
3. Se for um informe de venda (enviado por um vendedor), inclui a informação nos
dados do sistema e responder a mensagem contendo a string “OK” confirmando
a inclusão ou “ERRO” informando que os dados enviados estão incorretos.
4. Se for uma consulta (enviada por um gerente), identifica qual o tipo de consulta
solicitada, pesquisa e calcula nos dados acumulados a informação solicitada e
devolve a resposta adequada ou uma string “ERRO” informando que a
solicitação foi feita de forma incorreta (dados inválidos).
5. Responde a cada solicitação enviada

## Documentação:

### Este trabalho foi desenvolvido com a linguagem **PYTHON** versão 3, com a biblioteca *socket* para realizar a comunicação entre os processos.
<br/>

### É necessário ter o Python instalado na máquina, preferencialmente, na versão 3, para executar essa aplicação.
<br/>

### Estrutura do trabalho:
#### Essa solução foi divida em **três** arquivos:
* servidor.py
* gerente.py
* vendedor.py
<br/>

#### Instruções para rodar o projeto:
1. Clone este repositório com o comando: `git clone git@github.com:evertonnasac/socket-python.git` ou baixe os arquivos do projeto na opção *download.zip*
2. Utilize o terminal para ir até o diretório onde estão os arquivos do projeto.
3. Após se certificar que está trabalhando no diretório do projeto, deve-se, primeiramente, executar o servidor. Então, execute o comando python para executar o arquivo **servidor.py**. - Exemplo usando linux com python na versão 3: `python3 servidor.py`. 
4. Se tudo der certo, você verá, no terminal a mensagem: *Aguardando cliente...", isso significa que o servidor está sendo executado. Quando quiser encerrar o servidor, certifique-se que não há cliente conectado e digite as teclas CTRL+C
5. Este servidor atende a um cliente por vez, então, deve-se executar uma solução: *gerente* ou *vendedor* de cada vez.
6. Utilize outra janela do terminal para ir até o diretório deste projeto e executar o arquivo *gerente.py* ou *vendedor.py*.
7. Ao se certificar que está trabalhando no diretório do projeto, execute o comando python para executar, OU o arquivo **gerente.py** OU **vendedor.py** - Exemplo: `python3 gerente.py` se quiser trabalhar as funcionalidades do gerente ou `python3 vendedor.py` para as funcionalidades do vendedor.
8. Para encerrar um dos processos (citados no item 7) que tiver sendo executado, siga as instruções da aplicação ou digite as teclas CRTL+C e MANTENHA o servidor executando na outra janela, caso deseje continuar trabalhando com a aplicação.

## Sobre a aplicação:

### Para cumprir com os requisitos do projeto, a aplicação possui duas lojas previamente cadastradas, denominadas de LOJA_1 e LOJA_2.

### Há também 4 vendedores previamente cadastrados, denominados de:
* Joao 
* Ana
* Jose
* Maria

### Só é possível registrar vendas e realizar consultas com base nesses dados citados acima, não é possível inserir novos vendedores ou cadastrar novas lojas em tempo de execução.
<br/>

## Funcionalidades da solução Gerente: 
Tela de Menu:
![Menu gerente](/images/tela-menu-gerente.png)
<br/>

Opçao 1 - Total de um vendedor: <br/>
![Opcao 1](/images/tela-totalvendedor-gerente.png)
<br/>

Opção 2 - Maior vendedor: <br/>
![Opcao 2](/images/tela-maiorvendedor-gerente.png)
<br/>

Opcao 3 - Total de uma loja: <br/>
![Opcao 3](/images/tela-totalloja-gerente.png)
<br/>

Opcao 4 - Total da rede por período: <br/>
![opcao 4](/images/tela-totalredept1-gerente.png)
![opcao 4](/images/tela-totalredept2-gerente.png)
<br/>


Opcao 5 - Maior loja: <br/>
![opcao 5](/images/tela-maiorloja-gerente.png)
<br/>

## Funcionalidades da solução Vendedor:

Menu Vendedor: <br/>
![menu vendedor](/images/tela-menu-vendedor.png)
<br/>

Registrando venda do vendedor: <br/>
![menu vendedor](/images/tela-vendapt1-vendedor.png)
![menu vendedor](/images/tela-vendapt2-vendedor.png)
<br/>

Obs. Os testes acima foram realizados com os dados das vendas previamente cadastrados. <br/>
Utilize a solução *Vendedor* para alimentar a aplicação com os dados sobre as vendas, e poder, posteriormente, gerar os relatórios na solução *Gerente*, com base nos  dados que forem inseridos.

<br/>
<br/>
<br/>
<br/>

*Feito com* :heart:	