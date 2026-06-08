def ajuda(msg):
    while True:
        print('SISTEMA DE AJUDA PyHELP')
        comando = input(msg)
        if comando.upper() == 'FIM':
            print('\nENCERRANDO...')
            break
        else:
            print(f'\nAcessando o manual do comando "{comando}":\n')
            help(comando)


ajuda('Função ou Biblioteca > ')
