maior = menor = 0

for c in range(5):
    peso = float(input(f'Peso da {c + 1}ª pessoa: '))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}')
print(f'O menor peso lido foi de {menor}')
