import sys


def ler():
    try:
        response = input()
    except EOFError:
        sys.exit()

    return response


def viagemTarzan(cipos, distanciaLimite):
    x, y = 0, 1
    ciposOrigem = list(cipos)
    ciposDestino = list(cipos)

    for i in range(len(ciposOrigem)):
        pontoA = ciposOrigem[i]
        for j in range(len(ciposDestino)):
            pontoB = ciposDestino[j]
            if i != j:
                distancia = ((pontoB[x] - pontoA[x]) ** 2 + (pontoB[y] - pontoA[y]) ** 2) ** (1 / 2)
                print(pontoA)
                print(pontoB)
                print(distancia)
                if distancia > distanciaLimite:
                    return 'N'

    # for i in range(len(cipos) - 1):
    #     pontoA, pontoB = cipos[i], cipos[(i + 1)]
    #     print(pontoA)
    #     print(pontoB)
    #     distancia = ((pontoB[x] - pontoA[x]) ** 2 + ( pontoB[y] - pontoA[y]) ** 2) ** (1/2)
    #     print(distancia)
    #     if distancia > distanciaLimite:
    #         return 'N'

    return 'S'


def main():
    while True:
        floresta = ler()
        arvores, distancia = map(int, floresta.split(' '))

        cipos = []
        for i in range(arvores):
            ponto = ler()
            cipos.append(list(map(int, ponto.split(' '))))

        res = viagemTarzan(cipos, distancia)
        print(res)


if __name__ == '__main__':
    main()
