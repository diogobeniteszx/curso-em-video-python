matriz = []

soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

for l in range(3):
    linha = []
    for c in range(3):
        numero = int(input(f'Digite um número para [{l}, {c}]: '))
        linha.append(numero)
    matriz.append(linha)

print()

for l in range(3):
    for c in range(3):
        numero = matriz[l][c]
        print(f'{numero:^5}', end='')
        if numero % 2 == 0:
            soma_pares += numero
    print()

print(f'A soma dos valores pares é {soma_pares}.')

for l in range(3):
    soma_terceira_coluna += matriz[l][2]

maior_segunda_linha = matriz[1][0]
for c in range(1, 3):
    if matriz[1][c] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][c]

print(f'O maior valor da segunda linha é {maior_segunda_linha}.')
