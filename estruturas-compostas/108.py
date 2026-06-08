from pacote.modulos import moedas

preco = float(input('Digite o preço: R$'))

print(f'Aumentando 10%, temos {moedas.formatar(moedas.aumentar(preco, 10))}')
print(f'Diminuindo 10%, temos {moedas.formatar(moedas.diminuir(preco, 10))}')
print(f'O dobro de {moedas.formatar(preco)} é {moedas.formatar(moedas.dobrar(preco))}')
print(f'A metade de {moedas.formatar(preco)} é {moedas.formatar(moedas.metade(preco))}')
