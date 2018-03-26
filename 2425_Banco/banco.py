import sys


def ler():
    try:
        response = input()
    except EOFError:
        sys.exit()

    return response


def proximoCaixa(caixas):
    menorTempo = 0
    for i in range(len(caixas)):
        if caixas[i] < caixas[menorTempo]:
            menorTempo = i

    return menorTempo


def excedeAtendimento(caixa, clientes):
    caixas = [0] * caixa
    proximo = 0

    chegada, tempoAtendimento = 0, 1
    excederam = 0

    for cliente in clientes:
        tempoEspera = caixas[proximo] - cliente[chegada]

        if tempoEspera < 0:
            tempoEspera = 0

        caixas[proximo] = cliente[chegada] + cliente[tempoAtendimento] + tempoEspera
        proximo = proximoCaixa(caixas)

        if tempoEspera > 20:
            excederam += 1

    return excederam


def main():
    while True:
        agencia = ler()
        caixa, nCliente = map(int, agencia.split(' '))

        clientes = []
        for i in range(nCliente):
            cliente = ler()
            clientes.append(list(map(int, cliente.split(' '))))

        res = excedeAtendimento(caixa, clientes)
        print(res)


if __name__ == '__main__':
    main()
