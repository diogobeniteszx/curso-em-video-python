def notas(*valores, situacao=False):
    """
    Analisa um conjunto de notas e sua situação. 

    Parâmetros:
        *valores (float): Uma ou mais notas numéricas.
        situacao (bool, opcional): Se True, inclui a situação com base na média. Padrão é False.

    Retorna:
        dict: Um dicionário contendo:
            total (int): quantidade de notas.
            maior (float): maior nota.
            menor (float): menor nota.
            media (float): média das notas.
            situacao (str, opcional): avaliação da média ('Boa', 'Razoável' ou 'Ruim').
    """
    notas = {}
    notas['total'] = len(valores)
    notas['maior'] = max(valores)
    notas['menor'] = min(valores)
    notas['media'] = sum(valores) / len(valores)

    if situacao:
        if notas['media'] >= 7:
            notas['situacao'] = 'Boa'
        elif notas['media'] >= 5:
            notas['situacao'] = 'Razoável'
        else:
            notas['situacao'] = 'Ruim'

    return notas


resposta = notas(5.5, 2.5, 8.5, situacao=True)
print(resposta)
help(notas)
