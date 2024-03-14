import json

valores_moeda = ["1c", "2c", "5c", "10c", "20c", "50c", "1e", "2e"]

saldo = 100

def sair():
    global saldo
    if(saldo > 0):
        print(f"maq: O seu saldo é de {saldo}€. Obrigado pela preferência!")

def selecionar(stock, codigo):
    global saldo
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
            if saldo >= produto['preco']*100:
                saldo -= produto['preco']*100
                produto['quant'] -= 1
                #Escrever no ficheiro
                file = open("stock.json", "w")
                json.dump(stock, file, indent=4)
                file.close()
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
    global saldo
    print("cod |       nome       | quantidade | preço")
    print("--- |------------------|------------|------")
    for produto in stock:
        if produto['quant'] > 0:
            print(f"{produto['cod']} | {produto['nome']:16} | {produto['quant']:10} | {produto['preco']:5}")


def moeda(moedas, valores_moeda):
    global saldo
    for moeda in moedas:
        if moeda in valores_moeda:
            valor = int(moeda[:-1])
            if moeda[-1] == "c":
                saldo += valor
            else:
                saldo += valor*100
        else:
            print("Moeda inválida")
            return saldo

def working(stock, valores_moeda):
    global saldo
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
            selecionar(stock, codigo)
        
        elif entrada.startswith("MOEDA") :
            moedas = entrada.split(" ")[1:]
            moeda(moedas, valores_moeda)
                        
        else:
            print("Comando inválido")


if __name__ == "__main__":
    file = open("stock.json", "r")
    stock = json.load(file)
    file.close()
    working(stock, valores_moeda)
