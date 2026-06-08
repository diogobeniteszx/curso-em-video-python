def área(l, c):
    area = l * c
    return area


largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

print(f'Área: {área(largura, comprimento)} m²')
