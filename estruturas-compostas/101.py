def voto(ano):
    atual = 2025
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional!'
    else:
        return f'Com {idade} anos: Voto obrigatório!'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
