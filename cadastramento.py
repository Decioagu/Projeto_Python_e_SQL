import sqlite3
from pathlib import Path
from datetime import datetime

# --------------------------------------- CONFIGURAÇÃO DO BANCO DE DADOS ------------------------------------------

ROOT_DIR = Path(__file__).parent / 'BD' # pasta BD
DB_NAME = 'cadastro.sqlite3' # Nome do banco de dados
DB_FILE = ROOT_DIR / DB_NAME #  Caminho do arquivo banco de dados 'cadastro.sqlite3'

SELECAO_CANDIDATO = 'selecao_candidato' # Nome da tabela
SELECAO_TESTE = 'selecao_teste' # Nome da tabela

# Cria o diretório se não existir (pasta BD)
ROOT_DIR.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DB_FILE) # Conexão banco de dado (criar conexão)
cursor = connection.cursor() # Variável de controle (abrir conexão)

# ------------------------------------- CRIAR TABELAS NO BANCO DE DADOS -------------------------------------------

# Criar tabela 'selecao_candidato' em banco de dado SQLite
cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {SELECAO_CANDIDATO} (
    id_candidato INTEGER PRIMARY KEY AUTOINCREMENT,
    nme_candidato TEXT NOT NULL,
    dat_inscricao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """
)

# Criar tabela 'selecao_teste' em banco de dado SQLite
cursor.execute(
    f"""
    CREATE TABLE IF NOT EXISTS {SELECAO_TESTE} (
        id_teste INTEGER PRIMARY KEY AUTOINCREMENT,
        id_candidato INTEGER,
        num_fibonacci INTEGER NOT NULL,
        num_par INTEGER CHECK (num_par IN (0, 1)),
        num_impar INTEGER CHECK (num_impar IN (0, 1)),
        FOREIGN KEY (id_candidato) REFERENCES {SELECAO_CANDIDATO}(id_candidato)
    )
    """
)

connection.commit() # adicionar registros no banco de dados

# ----------------------------------- DATA E HORA | REGISTRO DAT_INSCRICAO ------------------------------------------

data_atual = datetime.now() # ano-mês-dia | hora:minuto:segundo:mile segundo (tipo:datetime)
data_formatada = data_atual.strftime('%d-%m-%Y %H:%M:%S') # dia-mês-ano | hora:minuto:segundo (tipo:string)

# ------------------------------------- INSERIR REGISTRO NO BANCO DE DADOS --------------------------------------------

# Inserir valores na tabela 'selecao_candidato'
sql_01 = (
    f"""INSERT INTO {SELECAO_CANDIDATO} 
        (nme_candidato, dat_inscricao) 
        VALUES 
        (:nome_candidato, :data_inscricao)""" # dicionario
)
# Dicionário com os dados do 'selecao_candidato'
dados_01 = {'nome_candidato': 'Décio Santana de Aguiar', 'data_inscricao' : data_formatada} 

# Inserir valores na tabela 'selecao_candidato' (executar comando)
cursor.execute(sql_01, dados_01) 

connection.commit() # adicionar registros no banco de dados

# ------------------------------------ REGRA DE NEGOCIO SEQUÊNCIA FIBONACCI ---------------------------------------------

lista_fibonacci = [] # Lista para armazenar os números da sequência de Fibonacci

# Gerar a sequência de Fibonacci
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        lista_fibonacci.append(a)
        a, b = b, a + b

fibonacci(30) # Gerar "N" termos da sequência de Fibonacci
# print(f'{lista_fibonacci=}') # Imprime a lista de Fibonacci

# Verificar se os números da lista de Fibonacci são pares (list comprehension)
verifica_num_par_lista_fibonacci = [1 if num % 2 == 0 else 0 for num in lista_fibonacci]
# print(f'{verifica_num_par_lista_fibonacci=}') # Imprime a lista de verificação de números pares

# Verificar se os números da lista de Fibonacci são ímpares (list comprehension)
verifica_num_impar_lista_fibonaccies = [1 if num % 2 != 0 else 0 for num in lista_fibonacci]
# print(f'{verifica_num_impar_lista_fibonaccies=}') # Imprime a lista de verificação de números ímpares

# ------------------------------------- INSERIR REGISTRO NO BANCO DE DADOS --------------------------------------------

# Inserir valores na tabela 'selecao_teste'
sql_02 = (
    f"""INSERT INTO {SELECAO_TESTE} 
    (id_candidato, num_fibonacci, num_par, num_impar) 
    VALUES 
    (?,?,?,?)""" # lista ou tupla
)

# Capturar o ultimo id_candidato inserido 
id_candidato = cursor.lastrowid

# lista de tuplas com os dados a serem inseridos na tabela 'selecao_teste'
dados_02 = [
    (id_candidato, fibonaccie, par, impar)
    for fibonaccie, par, impar in zip(lista_fibonacci, verifica_num_par_lista_fibonacci, verifica_num_impar_lista_fibonaccies)
] 

'''
    Em Python, a função zip() é uma função integrada que permite combinar 
    duas ou mais sequências (listas, tuplas, etc.) em um objeto zip.

    Exemplo:
    lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    lista2 = ['BA', 'SP', 'MG', 'RJ']
    lista3 = []

    zip_object = zip(lista1, lista2) # retorna um objeto Map
    print(zip_object) # <zip object at 0x000001A2B3C4D5E6>

    lista3 = [valor for valor in zip_object]  

    print(lista3) # (('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG'))
'''

# Inserir valores nas colunas da tabela tabela SQLite (executar comando)
cursor.executemany(sql_02, dados_02) # executemany() permite inserir múltiplos registros

connection.commit() # adicionar registros no banco de dados

# -------------------------------------- CONSULTA BANCO DE DADOS -------------------------------------------

def consultar_tabela_teste_num_fibonacci():
    """
    Função para consultar os dados de uma tabela específica no banco de dados SQLite.
    """
    # Consultar da tabela 'selecao_teste' no Banco de dados SQLite
    cursor.execute(f"SELECT num_fibonacci FROM {SELECAO_TESTE}")
    valores = cursor.fetchall() # Recupera todos os valores da coluna 'num_fibonacci' da tabela 'selecao_teste'

    lista_fibonacci = [valor[0] for valor in valores]  # Cria uma lista com os valores da sequência de Fibonacci

    print(f'{lista_fibonacci=}\n')  # Imprime a lista de Fibonacci

print()
consultar_tabela_teste_num_fibonacci()  # Chama a função para consultar a tabela 'selecao_teste'

# -------------------------------------- CONSULTA BANCO DE DADOS -------------------------------------------

# Consulta para pegar os 5 maiores valores da lista Fibonacci (num_fibonacci da tabela 'selecao_teste')
cursor.execute(
    f"""
    SELECT num_fibonacci 
    FROM {SELECAO_TESTE} 
    ORDER BY num_fibonacci DESC 
    LIMIT 5
    """)

maiores_numeros = cursor.fetchall() # Recupera os 5 maiores valores da coluna 'num_fibonacci' da tabela 'selecao_teste'

lista_dos_maiores_numeros_fibonacci = [valor[0] for valor in maiores_numeros]  # Cria uma lista com os valores da sequência de Fibonacci

print(f'{lista_dos_maiores_numeros_fibonacci=}\n')  # Imprime a lista de Fibonacci

# -------------------------------------- CONSULTA BANCO DE DADOS -------------------------------------------

# Contar números pares
cursor.execute(f"SELECT COUNT(*) FROM {SELECAO_TESTE} WHERE num_par = 1")
total_pares = cursor.fetchone()[0] # Recupera o total de números pares da tabela 'selecao_teste'

# Contar números ímpares
cursor.execute(f"SELECT COUNT(*) FROM {SELECAO_TESTE} WHERE num_impar = 1")
total_impares = cursor.fetchone()[0] # Recupera o total de números ímpares da tabela 'selecao_teste'

print(f'Quantidade de números "pares" armazenados na lista fibonacci: {total_pares}')
print(f'Quantidade de números "ímpares" armazenados na lista fibonacci: {total_impares}\n')

# ---------------------------------- DELETAR REGISTRO NO BANCO DE DADOS ------------------------------------

# Deletar todos os registros com num_fibonacci > 5000
cursor.execute(f"DELETE FROM {SELECAO_TESTE} WHERE num_fibonacci > 5000")

connection.commit() # adicionar registros no banco de dados

print("Os registros de números fibonacci maiores de 5000 foram deletados com sucesso!")

# -------------------------------------- CONSULTA BANCO DE DADOS -------------------------------------------

consultar_tabela_teste_num_fibonacci()  # Chama a função para consultar a tabela 'selecao_teste'

# --------------------------------- FECHAR CONEXÃO DO BANCO DE DADOS ---------------------------------------

cursor.close() # Fechar variável de controle
connection.close() # Fechar conexão com arquivo

