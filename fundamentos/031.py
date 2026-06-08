distancia = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km!')

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'O preço da passagem será R${preco:.2f}.')
