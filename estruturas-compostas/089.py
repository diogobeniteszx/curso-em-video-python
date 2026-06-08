ficha = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    resposta = input('Quer continuar? [S/N] ')
    if resposta.upper() == 'N':
        break

print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if 0 <= opcao < len(ficha):
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')

print('Volte sempre!')
