galera = []
soma_idade = 0

while True:
    pessoa = {}

    pessoa['nome'] = input('Nome: ')

    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']

    galera.append(pessoa.copy())

    while True:
        resp = input('Quer continuar? [S/N]: ').strip().upper()
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')

    if resp == 'N':
        break

total_pessoas = len(galera)
media_idade = soma_idade / total_pessoas

print(f'A) Ao todo temos {total_pessoas} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')

for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()

print('D) Lista das pessoas que estão acima da média:')

for p in galera:
    if p['idade'] >= media_idade:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k}: {v} ', end='')
        print()

print('\nENCERRADO')
