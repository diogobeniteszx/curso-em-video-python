from pacote.modulos.bib import *
from pacote.modulos.arquivo import *

arq = 'Cadastros.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas',
                    'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida.\033[m')
