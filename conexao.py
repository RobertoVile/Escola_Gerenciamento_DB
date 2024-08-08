import sqlite3


def conectar_banco():
    try:
        global conn
        conn = sqlite3.connect('teste.db')
        global cursor
        cursor = conn.cursor()
        print("Banco conectado com sucesso!")
        conn.commit()
    except sqlite3.Error as erro:
        print("Erro de conexão com o banco de dados!")
 