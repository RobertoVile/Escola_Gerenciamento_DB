import sqlite3
import conexao  
import tabela
def cadastro():
    try:
        # Conectar ao banco
        tabela.criar_tabela()
        # Coletar dados do usuário
        nome = input("Informe o nome completo do aluno: ")
        data = int(input("Informe o dia de nascimento do aluno (DD): "))
        mes = int(input("Informe o mês de nascimento do aluno (MM): "))
        ano = int(input("Informe o ano de nascimento do aluno (YYYY): "))
        cpf = int(input("Informe o CPF do aluno: "))
        telefone = input("Informe seu N° de Telefone (Responsável): ")
        email = input("Informe seu email (Responsável): ")
        endereco = input("Informe seu Endereço: ")
        nomeResponsavel = input("Informe o nome do responsável: ")
        nomeResponsavel2 = input("Informe o nome do segundo responsável (deixe em branco se não houver): ") or None

        #Insert
        inserir_aluno = """
        INSERT INTO teste (nome, data, mes, ano, cpf, telefone, email, endereco, nomeResponsavel, nomeResponsavel2)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        # Valores a serem inseridos
        valores = (
            nome,
            data,
            mes,
            ano,
            cpf,
            telefone,
            email,
            endereco,
            nomeResponsavel,
            nomeResponsavel2
        )

        #Executa o insert e passa os valores 
        conexao.cursor.execute(inserir_aluno, valores)
        conexao.conn.commit()

        print("O aluno foi cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar aluno!", erro)

    conexao.conn.close()
cadastro()
