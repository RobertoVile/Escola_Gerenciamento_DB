#Esboço da função para verificar se o usuário é funcionário ou responsável

def verificacao():
    print("Você é funcionário ou responsável?")
    opcaoI = input()
    if (opcaoI == 'responsável'):
        #Incluir a função de menu do responsável( ver o boletim do aluno).
        
    elif (opcaoI == 'funcionário'):
        #Incluir a função do menu do funcionário
        
    else:
        print('Opção inválida!')
        verificacao()