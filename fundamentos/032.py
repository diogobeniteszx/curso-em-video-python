ano = int(input('Que ano quer analizar? '))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if bissexto:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')
