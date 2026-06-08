while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    for c in range(1, 11):
        print(f'{valor} x {c} = {valor * c}')

print('Programa de tabuada encerrado. Volte sempre!')
