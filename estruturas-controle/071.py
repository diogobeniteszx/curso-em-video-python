print('{:^30}'.format('BANCO CEV'))

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
quantidade_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        quantidade_cedulas += 1
    else:
        if quantidade_cedulas > 0:
            print(f'Total de {quantidade_cedulas} cédulas de R${cedula}')
        
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        
        quantidade_cedulas = 0
        
        if total == 0:
            break

print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
