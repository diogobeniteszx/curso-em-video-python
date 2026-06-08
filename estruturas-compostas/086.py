matriz = []

for l in range(3):
    linha = []
    for c in range(3):
        numero = int(input(f'Número na posição [{l}, {c}]: '))
        linha.append(numero)
    matriz.append(linha)

print()

for linha in matriz:
    for numero in linha:
        print(f'{numero:^7}', end='')
    print()
