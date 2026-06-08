valores = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)

    resposta = input('Deseja continuar? [S/N] ')
    if resposta.upper() == 'N':
        break

cont = len(valores)
print(f'Você digitou {cont} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}.')

if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
