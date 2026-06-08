numero = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = 1

print(f'Calculando {numero}! = ', end='')

while numero > 0:
    print(numero, end=' ')
    print('x' if numero > 1 else '=', end=' ')
    fatorial *= numero
    numero -= 1

print(f'{fatorial}')
