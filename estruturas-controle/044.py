compras = float(input('Preço das compras: '))

print('Formas de pagamento:')
print('[1] À vista dinheiro/cheque')
print('[2] À vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')

opc = int(input('Opção: '))

if opc == 1:
    preco_final = compras * 0.90
elif opc == 2:
    preco_final = compras * 0.95
elif opc == 3:
    preco_final = compras
    valor_parcela = preco_final / 2
    print(f'Sua compra será parcelada em 2x de R${valor_parcela:.2f} sem juros.')
elif opc == 4:
    preco_final = compras * 1.20
    numero_parcelas = int(input('Número de parcelas: '))
    valor_parcela = preco_final / numero_parcelas
    print(f'Sua compra será parcelada em {numero_parcelas}x de R${valor_parcela:.2f} com juros.')
else:
    preco_final = compras
    print('Opção de pagamento inválida. Tente novamente.')

print(f'Sua compra de R${compras:.2f} vai custar R${preco_final:.2f} no final.')
