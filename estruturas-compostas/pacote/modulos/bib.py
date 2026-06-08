def leiaint(msg):
    while True:
        try:
            nint = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        else:
            return nint


def linha(tam=42):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc
