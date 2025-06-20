# Projeto_Python_e_SQL

- Prova de seleção para automatização de cadastro com script Python e SQLite:

- Arquivo em PDF: [Prova de seleção](Seleção.pdf)

- Sua empresa está realizando um processo seletivo e precisa automatizar parte do cadastro e
avaliação dos candidatos. Sua tarefa será criar um script Python que:

    1. Cria duas tabelas em um banco de dados Oracle com duas tabelas: SELECAO_CANDIDATO e
    SELECAO_TESTE .
    2. Insere um candidato fictício.
    3. Insere 30 registros na tabela SELECAO_TESTE , com base em regras específicas.
    4. Executa consultas SQL para análise.
    5. Segue boas práticas de programação.

- Descrição das Tabela SELECAO_CANDIDATO:
    - Coluna	            Tipo	        Regras
    - ID_CANDIDATO	        INTEGER	        Auto-incremento, chave primária
    - NME_CANDIDATO	        TEXT	        Nome do candidato
    - DAT_INSCRICAO	        TIMESTAMP	    Valor padrão: data e hora da inserção

- Descrição das Tabela SELECAO_TESTE:
    - Coluna	            Tipo	        Regras
    - ID_TESTE	            INTEGER	        Auto-incremento, chave primária
    - ID_CANDIDATO	        INTEGER	        Chave estrangeira referenciando SELECAO_CANDIDATO(ID_CANDIDATO)
    - NUM_FIBONACCI	        INTEGER	        Começa em 1, seguindo a sequência de Fibonacc
    - NUM_PAR	            INTEGER	        0 (falso) ou 1 (verdadeiro) – indica se o número é par
    - NUM_IMPAR	            INTEGER	        0 (falso) ou 1 (verdadeiro) – indica se o número é ímpar

1. Criação do Banco
    - Use sqlite3 para criar um banco de dados local.
    - Crie as duas tabelas com os campos acima, incluindo:
        - DAT_INSCRICAO com valor padrão de timestamp atual.
        - NUM_PAR e NUM_IMPAR com check constraint: só podem ter os valores 0 ou 1.

2. Inserção de Dados
    - Insira 1 registro fictício na tabela SELECAO_CANDIDATO com nome livre.
    - Insira 30 registros na tabela SELECAO_TESTE :
        - Cada linha corresponde a um número da sequência de Fibonacci.
        - Calcule para cada número se é par ou ímpar.
        - Preencha NUM_PAR com 1 se o número for par, 0 caso contrário.
        - Preencha NUM_IMPAR com 1 se o número for ímpar, 0 caso contrário.

3. Consultas SQL
    - Implemente consultas SQL, via Python, que:
    - Liste a sequência Fibonacci.
    - Liste os 5 maiores números da sequência inserida.
    - Conte quantos números pares e quantos ímpares foram armazenados.
    - Delete todos os números que forem maiores que 5000.
    - Liste a sequência Fibonacci.
