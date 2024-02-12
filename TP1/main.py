import sys

def main():
    f = sys.stdin
    dicionario = {}
    i = 0
    f.readline()
    validos = 0
    num_linhas = 0
    modalidades = []  # pos 8
    for linha in f:
        num_linhas += 1
        campos = linha.split(",")
        if campos[len(campos) - 1] == "true\n":
            validos += 1
        if campos[8] not in modalidades:
            modalidades.append(campos[8])
        if int(campos[5]) in dicionario:
            dicionario[int(campos[5])] += 1
        if int(campos[5]) not in dicionario:
            dicionario[int(campos[5])] = 1
    percentagem = (validos / num_linhas) * 100
    modalidades = sorted(modalidades)
    print("====MODALIDADES====")
    for modalidade in modalidades:
        print(modalidade)
    print("\n\n====ATLETAS====")
    print("Numero de atletas: ", num_linhas)
    print("Numero de atletas validos: ", validos)
    print("Percentagem de atletas validos: ", percentagem, "%")
    print("\n\n====IDADES====")
    dicionario = dict(sorted(dicionario.items()))
    maximo = max(dicionario.keys())
    # printar idade de 5 em 5 (0-4, 5-9, 10-14, etc)
    for i in range(0, maximo + 1, 5):
        valor = 0
        for j in range(i, i + 5):
            if j in dicionario:
                valor += dicionario[j]
        if valor != 0:
            print("[", i - 4, "-", i, "]:", valor)

if __name__ == "__main__":
    main()
