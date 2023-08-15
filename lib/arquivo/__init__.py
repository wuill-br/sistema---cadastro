from lib import interfaces
from lib.interfaces import cabeçalho

import sqlite3

# Criar uma função que recebe o nome e a idade como parâmetros
def inserir_dados(nome, idade):
  # Conectar ao banco de dados chamado dados.db
  conexao = sqlite3.connect("dados.db")
  # Criar um cursor para executar comandos SQL
  cursor = conexao.cursor()
  # Criar uma tabela chamada pessoas se ela não existir
  cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome TEXT, idade INTEGER)")
  # Inserir os dados na tabela usando uma tupla
  cursor.execute("INSERT INTO pessoas VALUES (?, ?)", (nome, idade))
  # Salvar as alterações no banco de dados
  conexao.commit()
  # Fechar a conexão
  conexao.close()

def mostrar_dados():
      # Conectar ao banco de dados chamado dados.db
      conexao = sqlite3.connect("dados.db")
      # Criar um cursor para executar comandos SQL
      cursor = conexao.cursor()
      # Selecionar todos os dados da tabela pessoas
      cursor.execute("SELECT * FROM pessoas")
      # Obter todos os registros como uma lista de tuplas
      registros = cursor.fetchall()
      # Percorrer a lista e mostrar cada registro na tela com print
      for registro in registros:
          # Desempacotar a tupla em duas variáveis
          nome, idade = registro
          # Formatar e imprimir a mensagem
          print(f"Nome: {nome}, Idade: {idade}")
      # Fechar a conexão
      conexao.close()



def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('ouve um erro ao criar aquivo')
    else:
        print(f'aquivo {nome} criado com sucesso')

def leraquivo(nome):
    try:

        a = open(nome,"rt")
    except:
        print('ouve um erro ao ler aquivo')

    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()



def cadastrar(arq, nome = 'desconhecido', idade=0):
   try:
        a = open(arq, 'at')
   except:
       print('ouve um erro ao tentar abrir o arquivo')

   else:
       try:
            a.write(f'{nome};{idade}\n')

       except:
           print('ouve um erro ao tentar escrever o aquivo')

       else:
           print(f'Novo registro de {nome} adicionado.')
           a.close()

