import sys


def ler():
    try:
        response = input()
    except EOFError:
        sys.exit()

    return response


def presenteNaAula(registros):
    # presentes = []
    # for i in registros:
    #     if i not in presentes:
    #         presentes.append(i)

    presentes = list(set(registros))
    return len(presentes)


def main():

    while True:
        tam = int(ler())
        # print(tam)
        registros = []
        for i in range(tam):
            registro = int(ler())
            registros.append(registro)

        # print(registros)

        res = presenteNaAula(registros)
        print(res)


if __name__ == '__main__':
    main()
