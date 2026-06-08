n = int(input('Digite um número: '))

divisivel = 0

for c in range(1, n + 1):
    if n % c == 0:
        print(c, end=' ')
        divisivel += 1

print()

print(f'O número {n} foi divisível {divisivel} vezes.')

if divisivel == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
