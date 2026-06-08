primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo_termo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{c} > ', end='')

print('ACABOU!')
