print('Gerador de PA')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

c = 0

while c < 10:
    print(f'{termo} → ', end='')
    termo += razao
    c += 1

print('Fim')
