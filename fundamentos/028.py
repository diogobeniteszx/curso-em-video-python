from random import randint

computador = randint(0, 5)
palpite = int(input('Em que número eu pensei de 0 a 5? '))

if palpite == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Errou! Eu pensei no número {computador} e não no {palpite}!')
