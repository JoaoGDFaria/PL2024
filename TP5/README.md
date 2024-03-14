# TP5

## Enunciado Vending Machine

Construir um programa de uma máquina de venda automática simulada com funcionalidades básicas de adicionar moedas, listar produtos, selecionar produtos e sair.
Foi desenvolvido com e sem analisador léxico.

## Ficheiro `vending_machine.py`

O ficheiro `vending_machine.py` implementa uma máquina de venda automática simulada. Este script oferece funcionalidades básicas para listar produtos, selecionar itens, inserir moedas e verificar o saldo.

### **Funcionalidades**

- Listar Produtos => Comando: `LISTAR`

Este comando exibe uma lista de produtos disponíveis, juntamente com suas quantidades e preços.

- Selecionar Produto => Comando: `SELECIONAR <código>`

Este comando permite selecionar um produto com base no seu código. Ele verifica se o produto está disponível e se há saldo suficiente para a compra.

- Inserir Moeda +> Comando: `MOEDA <moeda1> <moeda2> ...`

Este comando permite inserir moedas na máquina. Aceita moedas de 1c, 2c, 5c, 10c, 20c, 50c, 1€ e 2€.

- Sair => Comando: `SAIR`

Este comando finaliza a sessão na máquina de venda automática, exibindo o saldo final.



## Ficheiro `lex_vending_machine.py`

Este ficheiro tem as mesmas funcionalidades que o anterior, mas construído usando análise léxica.

### **Estrutura do Código**

1. **Definição de Tokens**: Definição dos tokens utilizados pelo analisador léxico.
2. **Expressões Regulares para Tokens**: Expressões regulares para cada token definido.
3. **Funções para Lidar com Tokens**: Funções para processar cada tipo de token, como adicionar moedas, listar produtos, selecionar um produto e sair da máquina.
4. **Função para Calcular Troco**: Função para calcular o troco com base no saldo atual, em caso de saída.
5. **Inicialização do Analisador Léxico**: Inicialização do analisador léxico fornecido pela biblioteca `ply`.
6. **Função Principal**: Função principal do programa que lê entrada do usuário e processa os tokens.

### **Principais Funcionalidades**
- **Adicionar Moedas**: O token `MOEDA` é usado para adicionar moedas à máquina, atualizando o saldo e exibindo o saldo atualizado.
- **Listar Produtos**: O token `LISTAR` permite listar os produtos disponíveis na máquina, exibindo seu código, nome, quantidade e preço.
- **Selecionar Produto**: O token `SELECIONAR` é usado para selecionar um produto com base em seu código, deduzindo o preço do saldo e atualizando o stock do produto no ficheiro JSON.
- **Calcular Troco**: A função `calcular_troco()` é chamada quando o usuário decide sair da máquina com saldo, calculando e exibindo o troco apropriado.
- **Ficheiro JSON**: O código faz uso de um arquivo JSON (`stock.json`) para armazenar e recuperar informações sobre o stock de produtos.


