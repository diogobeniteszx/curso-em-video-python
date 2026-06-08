from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opc = 0
while opc != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    opc = int(input('Qual é a sua opção? '))

    if opc == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')

    elif opc == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')

    elif opc == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = 'Ambos são iguais'
        print(f'Entre {n1} e {n2} o maior valor é {maior}')

    elif opc == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')

    print('-=' * 15)
    sleep(1)

print('Fim do programa! Volte sempre!')
