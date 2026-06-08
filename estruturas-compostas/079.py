valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = input('Deseja continuar? [S/N] ')
    if resposta.upper() == 'N':
        break

valores.sort()
print(f'Você digitou os valores: {valores}.')
