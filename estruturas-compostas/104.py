def leiaInt(msg):
    n = input(msg)
    while not n.isnumeric():
        n = input('Erro! Digite um número inteiro válido: ')
    return int(n)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
