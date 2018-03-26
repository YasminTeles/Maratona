import sys


def ler():
    try:
        response = input()
    except EOFError:
        sys.exit()

    return response


def passeioCavalo():
    return True


def main():
    while True:
        tam = int(ler())
        # print(tam)
        movimentos = []
        for i in range(tam):
            movimentos.append(int(ler()))

        # print(registros)

        res = passeioCavalo(movimentos)
        print(res)


if __name__ == '__main__':
    main()
