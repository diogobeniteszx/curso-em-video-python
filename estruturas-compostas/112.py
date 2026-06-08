from pacote.modulos import moedas, dados

preco = dados.leiaDinheiro('Digite o preço: R$')

moedas.resumir(preco, 20, 12)
