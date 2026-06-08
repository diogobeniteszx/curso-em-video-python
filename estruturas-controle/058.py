from random import randint

computador = randint(0, 10)

print('Sou seu computador... acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
tentativas = 0

while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Mais... Tente mais uma vez.')
        elif palpite > computador:
            print('Menos... Tente mais uma vez.')

print(f'Acertou com {tentativas} tentativas. Parabéns!')
