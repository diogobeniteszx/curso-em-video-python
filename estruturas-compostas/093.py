jogador = {}
gols_partidas = []

jogador['nome'] = input('Nome do jogador: ')
quantidade_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(quantidade_partidas):
    gols_partidas.append(int(input(f'Quantos gols na partida {c}? ')))

jogador['gols'] = gols_partidas[:]
jogador['total'] = sum(gols_partidas)

print(jogador)

for k, v in jogador.items():
    print(f'{k}: {v}')

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} fez {v} gols')

print(f'Foi um total de {jogador["total"]} gols')
