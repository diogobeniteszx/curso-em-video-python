soma = nome_maior_idade = idade_maior = mulheres_jovens = 0

for c in range(4):
    print(f'{c + 1}ª PESSOA')

    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower()

    soma += idade
    if sexo == 'm' and idade > idade_maior:
        idade_maior = idade
        nome_maior_idade = nome
    if sexo == 'f' and idade < 20:
        mulheres_jovens += 1

media = soma / 4

print(f'A média de idade do grupo é de {media:.2f} anos')
print(f'O homem mais velho tem {idade_maior} anos e se chama {nome_maior_idade}')
print(f'Ao todo são {mulheres_jovens} mulheres com menos de 20 anos')
