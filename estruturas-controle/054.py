from datetime import date

atual = date.today().year
maiores = menores = 0

for c in range(7):
    nascimento = int(input(f'Em que ano a {c + 1}ª pessoa nasceu? '))
    if atual - nascimento >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')
