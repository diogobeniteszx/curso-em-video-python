numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opc = int(input('Sua opção: '))

if opc == 1:
    print(f'{numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opc == 2:
    print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif opc == 3:
    print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('Opção inválida, tente novamente.')
