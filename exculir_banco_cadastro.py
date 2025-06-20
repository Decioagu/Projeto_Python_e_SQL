from pathlib import Path
import os

ROOT_DIR = Path(__file__).parent / 'BD' # pasta BD
DB_NAME = 'cadastro.sqlite3' # Nome do banco de dados
DB_FILE = ROOT_DIR / DB_NAME #  Caminho do arquivo banco de dados 'cadastro.sqlite3'

# Deletar arquivo do banco de dados se existir 'cadastro.sqlite3'
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)  
    print("Arquivo do banco de dados deletado com sucesso.")
else:
    print("Arquivo não encontrado.")
