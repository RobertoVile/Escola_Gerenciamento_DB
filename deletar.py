import sqlite3
import logging
import conexao
import tabela

# Função para excluir um aluno
def excluir_aluno():
    tabela.criar_tabela()
    # Digitar a matricula do aluno
    matricula = input("Informe a matricula do aluno que deseja excluir do sistema: ")
    usuario = "guilhermo"
    # Solicitar confirmação
    confirmacao = input(f'Você tem certeza que deseja excluir o aluno com matricula {matricula}? (s/n): ')
    if confirmacao.lower() != 's':
        logging.info('Exclusão cancelada pelo usuário.')
        print("Exclusão cancelada.")

    # Verifique se o usuário tem permissão
    """if not usuario.tem_permissao('excluir_aluno'):
        logging.warning(f'Usuário {usuario.nome} não tem permissão para excluir alunos.')
        print("Você não tem permissão para realizar esta operação.")"""

    # Tentar excluir o aluno
    conn = conexao.conectar_banco()
    cursor = conexao.conn.cursor()
    try:
        cursor.execute('SELECT * FROM teste WHERE matricula = ?', (matricula,))
        aluno = cursor.fetchone()
        
        if aluno:
            cursor.execute('DELETE FROM teste WHERE matricula = ?', (matricula,))
            conexao.conn.commit()
            logging.info(f'Aluno com matricula {matricula} foi excluído por {usuario}.')
            print("Aluno excluído com sucesso.")
        else:
            logging.warning(f'Aluno com matricula {matricula} não encontrado.')
            print("Aluno não encontrado.")
    except sqlite3.Error as erro:
        print("Erro ao excluir aluno:",erro)
    finally:
        conexao.conn.close()

excluir_aluno()
        
