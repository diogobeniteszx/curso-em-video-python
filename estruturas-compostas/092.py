from datetime import datetime

dados = {}
dados['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano_nascimento

dados['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + \
        ((dados['contratacao'] + 35) - datetime.now().year)

for k, v in dados.items():
    print(f'{k}: {v}')
