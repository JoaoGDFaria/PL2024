import json
import ply.lex as lex
import re

saldo = 0
stock = []

# Definindo os tokens
tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR'
)

# Ignorando caracteres de espaço em branco
t_ignore = ' \t\n'

# Expressões regulares para os tokens
def t_MOEDA(t):
    r'MOEDA\s+(1[ce]|2[ce]|5c|10c|20c|50c)'
    global saldo

    valor_moeda = t.value.split()[1]
    if valor_moeda == "1e":
        saldo += 100
    elif valor_moeda == "2e":
        saldo += 200
    elif valor_moeda == "5c":
        saldo += 5
    elif valor_moeda == "10c":
        saldo += 10
    elif valor_moeda == "20c":
        saldo += 20
    elif valor_moeda == "50c":
        saldo += 50
    print(f"maq: Saldo = {saldo//100}e {saldo%100}c")

# Função para lidar com erros de token
def t_error(t):
    t.lexer.skip(1)

# Expressão regular para a regra 'SAIR'
def t_SAIR(t):
    r'SAIR'
    global saldo
    if saldo == 0:
        print("maq: Sem troco, saindo.")
        exit()
    else:
        resp = calcular_troco()
        print(f"maq: Pode retirar o troco: {resp}")
        print("maq: Até à próxima.")
        exit()

# Expressão regular para a regra 'LISTAR'
def t_LISTAR(t):
    r'LISTAR'
    global stock
    print("cod |       nome       | quantidade | preço")
    print("--- |------------------|------------|------")
    for produto in stock:
        if produto['quant'] > 0:
            print(f"{produto['cod']} | {produto['nome']:16} | {produto['quant']:10} | {produto['preco']:5}")

# Expressão regular para a regra 'SELECIONAR'
def t_SELECIONAR(t):
    r'SELECIONAR\s[A-Z]\d{2}'
    global saldo
    ide = t.value.split()[1]
    for elem in stock:
        if elem['cod'] == ide:
            if elem['quant'] > 0:
                if saldo >= elem['preco']*100:
                    print(f"Produto selecionado: {elem['nome']}")
                    elem['quant'] -= 1
                    with open("stock.json", "w") as f:
                        json.dump(stock, f, indent=4)
                    saldo -= elem['preco']*100

                    print(f"Produto entregue: {elem['nome']}")
                    print(f"maq: Saldo = {saldo//100}e {saldo%100}c")

                else:
                    print(f"Saldo insuficiente: {saldo//100}e {saldo%100}c para valor do produto: {elem['preco']}e")

            else:
                print(f"Produto esgotado: {elem['nome']}")
            break
    else:
        print(f"Produto inexistente: {ide}")
    return t

# Função para calcular o troco
def calcular_troco():
    global saldo
    moedas = {
        200: '2e', 100: '1e', 50: '50c', 20: '20c', 10: '10c',
        5: '5c', 2: '2c', 1: '1c'
    }
    
    troco = {}
    if saldo > 0:
        for valor_moeda in sorted(moedas.keys(), reverse=True):
            if saldo >= valor_moeda:
                quantidade = saldo // valor_moeda
                troco[moedas[valor_moeda]] = quantidade
                saldo -= quantidade * valor_moeda

    return troco

# Inicializando o analisador léxico
lexer = lex.lex()

# Função principal
def main():
    global stock
    global saldo

    with open('stock.json', 'r') as f:
        stock = json.load(f)
    
    while True:
        try:
            s = input()
        except EOFError:
            break
        lexer.input(s)
        for _ in lexer:
            pass

if __name__ == "__main__":
    main()
