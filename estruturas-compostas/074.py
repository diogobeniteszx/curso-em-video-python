from random import randint

valores = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10)
)

print('Valores sorteados:', end=' ')
for valor in valores:
    print(valor, end=' ')

print(f'\nMaior valor sorteado: {max(valores)}')
print(f'Menor valor sorteado: {min(valores)}')
