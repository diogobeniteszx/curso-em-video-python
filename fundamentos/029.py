velocidade = int(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Multado! Você excedeu o limite permitido que é 80Km/h.')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
