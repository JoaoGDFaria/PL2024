import sys

def main(file):
    f = open(file[1], "r")
    dicionario = {}
    i=0
    f.readline()
    validos = 0
    num_linhas = 0
    modalidades = [] #pos 8
    for linha in f:
        num_linhas += 1
        campos = linha.split(",")
        if campos[len(campos)-1] == "true\n":
            validos += 1
        if campos[8] not in modalidades:
            modalidades.append(campos[8])
        if int(campos[5]) in dicionario:
            dicionario[int(campos[5])] += 1
        else:
            dicionario[int(campos[5])] = 1
    percentagem = (validos/num_linhas)*100
    modalidades = sorted(modalidades)
    print("====MODALIDADES====")
    for modalidade in modalidades:
        print(modalidade)
    print("\n\n====ATLETAS====")
    print("Numero de atletas: ", num_linhas)
    print("Numero de atletas validos: ", validos)
    print("Percentagem de atletas validos: ", percentagem, "%")
    print("\n\n====IDADES====")
    di = {}
    for i in range(4, 101, 5):
        di[i] = 0
    for idade in dicionario:
        for i in range(4, 101, 5):
            if idade >= i and idade < i+4:
                di[i] += dicionario[idade]
    for idade in di:
        if di[idade] != 0:
            print("[",idade-4,"-", idade, "]:", di[idade])


if __name__ == "__main__":
    main(sys.argv)