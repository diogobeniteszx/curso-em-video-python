from random import randint

jogos = []
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

while total <= quantidade:
    jogo = []
    while len(jogo) < 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogo.sort()
    jogos.append(jogo)
    total += 1

print(f'Sorteando {quantidade} jogos:')
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
print('Boa sorte!')
