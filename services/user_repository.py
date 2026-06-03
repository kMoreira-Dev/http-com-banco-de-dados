# IMPORTACOES
import sqlite3
from pathlib import Path

# SALVAR O BANCO DE DADOS NAS PASTA DATABASE
path_dir = Path(__file__).resolve().parent.parent

db_path = path_dir / 'database' /  'users.db'

# CRIAR CONEXAO COM BANCO DE DADOS
conexao = sqlite3.connect(
    db_path,
    check_same_thread=False
)

# CONFIGURAR O CURSOR PARA RETORNAR DICIONARIOS
conexao.row_factory = sqlite3.Row

# CRIAR CURSOR PARA EXECUTAR COMANDOS SQL
cursor = conexao.cursor()

# CRIAR TABELA DE USUARIOS
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
    )
''')

# CRIACAO DE USUARIOS
def create_user(name, email):
    
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)',
        (name, email))

    conexao.commit()

    return {
            "message": "User created successfully!"
        }


# LEITURA DE USUARIOS
def get_users():

    cursor.execute('SELECT * FROM users ORDER BY id')

    users = cursor.fetchall()

    return [dict(user) for user in users]

# ATUALIZAR USUARIOS
def update_user(user_id, name, email):

    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?',
    (name, email, user_id))

    conexao.commit()
        
    if cursor.rowcount == 0:

        return {
            "message": f"User with id {user_id} not found."
        }

    return {
            "message": f"User with id {user_id} updated successfully."
        }

# DELETAR USUARIOS
def delete_user(user_id):

    cursor.execute('DELETE FROM users WHERE id = ?',
    (user_id,))

    conexao.commit()

    if cursor.rowcount == 0:
        
        return {
            "message": f"User with id {user_id} not found."
        }

    return {
            "message": f"User with id {user_id} deleted successfully."
        }