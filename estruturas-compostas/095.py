time = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome: ')
    quantidade_partidas = int(
        input(f'Quantas partidas {jogador["nome"]} jogou? '))

    partidas = []
    for c in range(quantidade_partidas):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = input('Continuar? [S/N]: ').strip().upper()
        if resp in 'SN':
            break
        print('Erro! Responda S ou N.')

    if resp == 'N':
        break

print('Código ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? ([999] para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}.')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, gols in enumerate(time[busca]['gols']):
            print(f' No jogo {i + 1} fez {gols} gols')
print('Volte sempre!')
