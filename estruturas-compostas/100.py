from random import randint


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for _ in range(5):
        numero = randint(1, 10)
        lista.append(numero)
        print(numero, end=' ')
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
