peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO do peso normal!')
elif imc < 25:
    print('Parabéns, você está no peso normal!')
elif imc < 30:
    print('Você está com SOBREPESO!')
elif imc < 40:
    print('Você está OBESO!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
