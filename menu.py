def menu():
    #Menu do gerenciamento do banco de dados da academia
    print("########### 'Nome da Escola' ############")
    print("O que deseja fazer:")
    print(""" 1 - Cadastrar Aluno:
          \n 2 - Exibir Quantidade de Alunos:
          \n 3 - Consultar Aluno pelo ID:
          \n 4 - Alterar Dados Cadastrais:
          \n 5 - Excluir Aluno:
          \n 6 - Sair""")
    print("############################################")
    #Declaração, valor e retorno da função opcao para inclui-lá no arquivo main.
    global opcao
    opcao = input()
    return opcao