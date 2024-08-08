import conexao

def criar_tabela():
    conexao.conectar_banco()
    criar_tabela = "CREATE TABLE IF NOT EXISTS teste (matricula INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, data INTEGER, mes INTEGER, ano INTEGER, cpf INTEGER, telefone INTEGER, email TEXT, endereco TEXT, nomeResponsavel TEXT, nomeResponsavel2 TEXT)"
    conexao.cursor.execute(criar_tabela)
    print("tabela criada")

criar_tabela()