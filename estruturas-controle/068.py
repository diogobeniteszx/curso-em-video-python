from random import randint

vitorias = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = input('Par ou Impar? [P/I] ').strip().upper()[0]
    
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('deu par' if total % 2 == 0 else 'deu ímpar')
    
    if escolha == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    
    print('Vamos jogar novamente!')

print(f'Game over! Você venceu {vitorias} vezes.')
