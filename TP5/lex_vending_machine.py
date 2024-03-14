import json
import ply.lex as lex

saldo = 0

#VENDING MACHINE LEXER
tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR'
)

t_LISTAR = r'LISTAR'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'

t_ignore = " \t"

def calcular_troco():
    global saldo
   
    # Dicionário com os valores das moedas em centavos e euros
    moedas = {
        200: '2e', 100: '1e', 50: '50c', 20: '20c', 10: '10c',
        5: '5c', 2: '2c', 1: '1c'
    }
    
    troco = {}
    
    for valor_moeda in sorted(moedas.keys(), reverse=True):
        if saldo >= valor_moeda:
            quantidade = saldo // valor_moeda
            troco[moedas[valor_moeda]] = quantidade
            saldo -= quantidade * valor_moeda
    
    return troco



def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_MOEDA(t):
    #MOEDA 5c, 10c, 25c, 50c, 1e, 2e
    r"MOEDA (5c|10c|25c|50c|1e|2e)+"

def t_SAIR(t):
    global saldo
    r"SAIR"
    if saldo == 0:
        print("maq: Sem troco, saíndo.")
        exit()
    else:
        resp = calcular_troco()


lexer = lex.lex()

def main():
    json_file = open("stock.json", "r")
    stock = json.load(json_file)

    while True:

