def aumentar(preco=0, percentual=0, formato=False):
    """
    Calcula o aumento de um valor com base em um percentual.

    Parâmetros:
        preco (float, opcional): Valor original. Padrão é 0.
        percentual (float, opcional): Percentual de aumento. Padrão é 0.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda. Padrão é False.

    Retorna:
        float ou str: Valor aumentado, com ou sem formatação.
    """
    resposta = preco + (preco * percentual / 100)
    return formatar(resposta) if formato else resposta


def diminuir(preco=0, percentual=0, formato=False):
    """
    Calcula a redução de um valor com base em um percentual.

    Parâmetros:
        preco (float, opcional): Valor original. Padrão é 0.
        percentual (float, opcional): Percentual de redução. Padrão é 0.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda. Padrão é False.

    Retorna:
        float ou str: Valor reduzido, com ou sem formatação.
    """
    resposta = preco - (preco * percentual / 100)
    return formatar(resposta) if formato else resposta


def dobrar(preco=0, formato=False):
    """
    Calcula o dobro de um valor.

    Parâmetros:
        preco (float, opcional): Valor original. Padrão é 0.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda. Padrão é False.

    Retorna:
        float ou str: Dobro do valor, com ou sem formatação.
    """
    resposta = preco * 2
    return formatar(resposta) if formato else resposta


def metade(preco=0, formato=False):
    """
    Calcula a metade de um valor.

    Parâmetros:
        preco (float, opcional): Valor original. Padrão é 0.
        formato (bool, opcional): Se True, retorna o valor formatado como moeda. Padrão é False.

    Retorna:
        float ou str: Metade do valor, com ou sem formatação.
    """
    resposta = preco / 2
    return formatar(resposta) if formato else resposta


def formatar(preco=0, moeda='R$'):
    """
    Formata um número como valor monetário.

    Parâmetros:
        preco (float, opcional): Valor numérico a ser formatado. Padrão é 0.
        moeda (str, opcional): Símbolo da moeda. Padrão é 'R$'.

    Retorna:
        str: Valor formatado no padrão monetário brasileiro.
    """
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumir(preco=0, aumento=10, reducao=5):
    """
    Exibe um resumo com os principais cálculos sobre o valor informado.

    Parâmetros:
        preco (float, opcional): Valor original. Padrão é 0.
        aumento (float, opcional): Percentual de aumento. Padrão é 10.
        reducao (float, opcional): Percentual de redução. Padrão é 5.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{formatar(preco)}')
    print(f'Dobro do preço: \t{dobrar(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução:  \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
