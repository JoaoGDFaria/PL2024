stock = [
    {"cod": "A23", "nome": "água", "quant": 8, "preco": 0.7},
    {"cod": "B15", "nome": "refrigerante", "quant": 10, "preco": 1.2},
    {"cod": "C02", "nome": "café", "quant": 6, "preco": 1.0},
    {"cod": "D08", "nome": "presunto", "quant": 5, "preco": 2.5},
    {"cod": "E10", "nome": "chocolate", "quant": 7, "preco": 1.5},
    {"cod": "F04", "nome": "rissol", "quant": 9, "preco": 1.0},
    {"cod": "G12", "nome": "cereais", "quant": 4, "preco": 0.8},
    {"cod": "H09", "nome": "iogurte", "quant": 8, "preco": 1.3},
    {"cod": "I11", "nome": "maçã", "quant": 10, "preco": 0.6},
    {"cod": "J05", "nome": "banana", "quant": 7, "preco": 0.5},
    {"cod": "K07", "nome": "biscoito", "quant": 6, "preco": 1.0},
    {"cod": "L13", "nome": "sopa", "quant": 5, "preco": 1.2},
    {"cod": "M01", "nome": "amendoins", "quant": 8, "preco": 0.9},
    {"cod": "N03", "nome": "batatas", "quant": 7, "preco": 1.0},
    {"cod": "O06", "nome": "barrinha", "quant": 6, "preco": 1.2},
    {"cod": "P14", "nome": "sumo", "quant": 9, "preco": 1.0},
    {"cod": "Q02", "nome": "pipoca", "quant": 8, "preco": 1.5},
    {"cod": "R08", "nome": "bolacha belga", "quant": 7, "preco": 1.2},
    {"cod": "S10", "nome": "tigela de frutas", "quant": 5, "preco": 2.0},
    {"cod": "T15", "nome": "sanduíche", "quant": 6, "preco": 2.5},
    {"cod": "U13", "nome": "bolo", "quant": 7, "preco": 0.8},
]

valores_moeda = ["1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e"]

saldo_inicial = 0

def sair(saldo):
    if(saldo > 0):
        print(f"maq: O seu saldo é de {saldo}€. Obrigado pela preferência!")

def selecionar(stock, codigo, saldo):
    produto = None
    for p in stock:
        if p['cod'] == codigo:
            produto = p
            break
    if produto is None:
        print("Produto não encontrado")
        return
    else:
        if produto['quant'] > 0:
            if saldo >= produto['preco']:
                saldo -= produto['preco']*100
                produto['quant'] -= 1
                if saldo < 100:
                    print(f"maq: Produto {produto['nome']} selecionado. Saldo restante: {saldo}c")
                    return saldo
                else:
                    print(f"maq: Produto {produto['nome']} selecionado. Saldo restante: {saldo//100}e {saldo%100}c")
                    return saldo
            else:
                print("maq: Saldo insuficiente para satisfazer o pedido")
                if saldo < 100 and produto['preco'] < 100:
                    text_saldo = f"{saldo}c"
                    text_preco = f"{produto['preco']}c"
                
                elif saldo >= 100 and produto['preco'] < 100:
                    text_saldo = f"{saldo//100}e {saldo%100}c"
                    text_preco = f"{produto['preco']}c"
                
                elif saldo < 100 and produto['preco'] >= 100:
                    text_saldo = f"{saldo}c"
                    text_preco = f"{produto['preco']//100}e {produto['preco']%100}c"
                
                else:
                    text_saldo = f"{saldo//100}e {saldo%100}c"
                    text_preco = f"{produto['preco']//100}e {produto['preco']%100}c"
                
                print(f"maq: Saldo = {text_saldo}, Valor do pedido = {text_preco}€")
                return saldo

        else:
            print("Produto esgotado")
            return saldo
        


def listar(stock):
    #Criar tabela com espaços iguais para cada coluna e texto centrado
    print("cod |       nome       | quantidade | preço")
    print("--- |------------------|------------|------")
    for produto in stock:
        if produto['quant'] > 0:
            print(f"{produto['cod']} | {produto['nome']:16} | {produto['quant']:10} | {produto['preco']:5}")


def working(stock, valores_moeda):
    saldo = saldo_inicial
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("==========VENDING MACHINE==========")
    while(True):
        entrada = input(">>> ")
        if entrada == "LISTAR" :
            listar(stock)
        elif entrada == "SAIR" :
            saldo = sair(saldo)
        elif entrada.startswith("SELECIONAR") :
            codigo = entrada.split(" ")[1]
            selecionar(stock, codigo, saldo)
                        
        else:
            print("Comando inválido")


if __name__ == "__main__":
    working(stock, valores_moeda)
