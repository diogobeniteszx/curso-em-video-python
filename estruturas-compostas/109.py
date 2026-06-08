from pacote.modulos import moedas

preco = float(input('Digite o preço: R$'))

print(f'Aumentando 10%, temos {moedas.aumentar(preco, 10, True)}')
print(f'Diminuindo 10%, temos {moedas.diminuir(preco, 10, True)}')
print(f'O dobro de {moedas.formatar(preco)} é {moedas.dobrar(preco, True)}')
print(f'A metade de {moedas.formatar(preco)} é {moedas.metade(preco, True)}')
