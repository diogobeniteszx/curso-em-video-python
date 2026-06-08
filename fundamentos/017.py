oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (oposto ** 2 + adjacente ** 2) ** 0.5
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')
