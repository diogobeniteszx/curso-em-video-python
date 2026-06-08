from random import shuffle

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')

alunos = [primeiro, segundo, terceiro, quarto]
shuffle(alunos)

print('A ordem de apresentação será:')
print(alunos)
