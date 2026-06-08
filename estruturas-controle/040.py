nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média é {media:.1f}.')

if media >= 7:
    print('Aluno aprovado!')
elif media >= 5:
    print('Aluno em recuperação!')
else:
    print('Aluno reprovado!')
