itens = (
    'lápis', 1.75,
    'borracha', 2.00,
    'caderno', 15.90,
    'estojo', 25.00,
    'transferidor', 4.20,
    'compasso', 9.99,
    'mochila', 120.32,
    'canetas', 22.30,
    'livro', 34.90
)

print(f'{"LISTAGEM DE PREÇOS":^40}')

for c in range(0, len(itens), 2):
    nome = itens[c]
    preco = itens[c + 1]
    print(f'{nome.title():.<30}R$ {preco:>6.2f}')
