from random import randint

opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = int(input('Qual a sua jogada? '))

if jogador < 0 or jogador > 2:
    print('JOGADA INVÁLIDA!')
else:
    print(f'O computador escolheu {opcoes[computador]}.')
    print(f'Você escolheu {opcoes[jogador]}.')

    if computador == jogador:
        print('EMPATE!')
    elif (computador == 0 and jogador == 1) or \
         (computador == 1 and jogador == 2) or \
         (computador == 2 and jogador == 0):
        print('VOCÊ VENCEU!')
    else:
        print('VOCÊ PERDEU!')
