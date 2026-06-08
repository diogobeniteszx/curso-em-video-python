def leiaInt(msg):
    while True:
        try:
            nint = int(input(msg))
        except:
            print('Erro! Digite um número inteiro válido.')
        else:
            return nint


def leiaFloat(msg):
    while True:
        try:
            nreal = float(input(msg))
        except:
            print('Erro! Digite um número inteiro válido.')
        else:
            return nreal


nint = leiaInt('Digite um número inteiro: ')
nreal = leiaFloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {nint} e o real foi {nreal}')
