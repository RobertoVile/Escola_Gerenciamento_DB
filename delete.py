import sqlite3


#Função deletar_aluno
def deletar_aluno():
    #Conectando a conexão
    conexao.conectar()
    #Pegando ID dos dados
    id = input("Informe o ID que deseja deletar: ")
    
    try:
        #Buscando ID do aluno
        resultado = conexao.dados.execute('''SELECT * FROM cliente where id = ?''',(id),).fetchall()
        #Se o ID for falso cai nessa função
        if(resultado == []):
            print("ID não encontrado!")
        #Se o ID for verdadeiro ira ser deletado
        else:
            #Conexão da tabela
            dados=sqlite3.connect('.db')
            
            cursor = dados.cursor()
            #Buscando o ID
            cursor.execute("DELETE FROM cliente WHERE id = '"+id+"'")
            #Atualização dos dados/Fechar os dados
            dados.commit()
            dados.close
            print("Dado excluído com sucesso!")
             
    except Exception as erro:
        print("Erro ao excluir dados: ", erro)