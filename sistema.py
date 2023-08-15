from time import sleep

from lib.arquivo import *
from lib.interfaces import *

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)


cabeçalho('Sistema de Cadastro V.1.0')
while True:
    resp = menu(['Ver Pessoas Cadastrada','Cadastrar pessoa','sair do programa'])
    if resp == 1:
        mostrar_dados()
        cabeçalho('Opcão 1')
        sleep(1)
    elif resp == 2:
        cabeçalho('Novo Cadastro')
        nome=str(input("Nome:"))
        idade=leiaint('Idade:')
        inserir_dados(nome, idade)
        #cadastrar(arq,nome,idade)
    elif resp == 3:
        cabeçalho('Saindo do program ....ate logo')
        break
    else:
        print('\033[31mErro ! Digite uma opçao válida!\033[m')
        sleep(1)

