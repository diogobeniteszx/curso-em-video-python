valores = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número: '))
    valores.append(numero)

    resposta = input('Deseja continuar? [S/N] ')
    if resposta.upper() == 'N':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'A lista completa é: {valores}.')
print(f'A lista de pares é: {pares}.')
print(f'A lista de ímpares é: {impares}.')
