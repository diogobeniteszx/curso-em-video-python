valores = (
    int(input('Número: ')),
    int(input('Outro número: ')),
    int(input('Mais um número: ')),
    int(input('Último número: '))
)

print(f'Você digitou os valores {valores}.')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    posicao = valores.index(3) + 1
    print(f'O valor 3 apareceu na {posicao}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Valores pares:', end=' ')
for par in valores:
    if par % 2 == 0:
        print(par, end=' ')
