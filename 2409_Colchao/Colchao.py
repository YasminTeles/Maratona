import sys
from sys import version_info


def passaPelaPorta(colchao, porta):
    if porta[0] > porta[1]:
        maior = porta[0]
        menor = porta[1]
    else:
        maior = porta[1]
        menor = porta[0]

    colchao_ordenado = sorted(colchao)
    tam = len(colchao_ordenado)
    resultMenor = False
    resultMaior = False

    for i in range(tam):
        if menor >= colchao_ordenado[i]:
            colchao_ordenado[i] = 'x'
            resultMenor = True
            break

    for i in range(tam):
        if colchao_ordenado[(i - tam)] != 'x' and (maior >= colchao_ordenado[(i - tam)]):
            colchao_ordenado[(i - tam)] = 'x'
            resultMaior = True
            break

    if resultMaior and resultMenor:
        return "S"
    else:
        return "N"


def ler():
    try:
        response = input()
    except EOFError:
        sys.exit()

    return response


def main():

    while True:
        colchao = ler()
        colchao = list(map(int, colchao.split(' ')))
        # print(colchao)

        porta = ler()
        porta = list(map(int, porta.split(' ')))
        # print(porta)

        res = passaPelaPorta(colchao, porta)
        print(res)


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     main(int(sys.argv[1]))
    main()
