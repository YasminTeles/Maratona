import sys


def ler():
    try:
        response = input()
    except EOFError:
        sys.exit()

    return response


def buscarCasa(casa, vizinhanca):
    meio = int(len(vizinhanca) / 2)
    if casa == vizinhanca[meio]:
        return True

    if len(vizinhanca) > 1:
        if casa < vizinhanca[meio]:
            return buscarCasa(casa, vizinhanca[:meio])
        else:
            return buscarCasa(casa, vizinhanca[meio:])
    else:
        return False


def encontrarBrinquedo(dica, vizinhanca):
    meio = int(dica / 2) + (dica % 2)
    casaA = vizinhanca[0]
    casaB = vizinhanca[len(vizinhanca) - 1]
    i = casaA

    while i < meio and j < casaB:



    for i in range(meio):
        sugestaoA, sugestaoB = i, (dica - i)
        if buscarCasa(casaA, vizinhanca) and buscarCasa(casaB, vizinhanca):
            break

    return str(casaA) + " " + str(casaB)


def main():
    while True:
        vizinhanca = int(ler())
        casas = []
        for i in range(vizinhanca):
            casas.append(int(ler()))

        dica = int(ler())

        res = encontrarBrinquedo(dica, casas)
        print(res)


if __name__ == '__main__':
    main()
