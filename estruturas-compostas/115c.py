from pacote.modulos.bib import *
from pacote.modulos.arquivo import *
from time import sleep

arq = 'Cadastros.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas',
                    'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo.
        ler_arquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de Sair do sistema.
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mErro! Digite uma opção válida.\033[m')
    sleep(1)
