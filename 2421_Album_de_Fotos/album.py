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


# def colarFoto(album, fotoA, fotoB):
#     largura, altura = 0, 1
#     for i in range(2):
#         for j in range(2):
#             if fotoA[i] + fotoB[j] <= album[largura]:
#
#             if fotoA[i] + fotoB[j] <= album[altura]:


def main():
    while True:
        album = list(map(int, ler().split(' ')))
        fotoA = list(map(int, ler().split(' ')))
        fotoB = list(map(int, ler().split(' ')))

        res = colarFoto(album, fotoA, fotoB)
        print(res)


if __name__ == '__main__':
    main()
