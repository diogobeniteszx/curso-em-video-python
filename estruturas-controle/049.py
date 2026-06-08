n = int(input('Número para ver a tabuada: '))

for c in range(1, 11):
    resultado = c * n
    print(f'{n} x {c:2} = {resultado}')
