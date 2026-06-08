largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
litros = area / 2

print(f'Sua parede tem a dimensão de {largura} x {altura} e a área é {area} m².')
print(f'Para pintar essa parede, você precisará de {litros} litros de tinta.')
