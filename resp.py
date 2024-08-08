def responsavel2():
        global nomeResponsavel2
        verResponsavel = input("Há outro responsável? ").lower()
        if verResponsavel == 'sim':
            nomeResponsavel2 = input("Qual o nome do segundo responsável? ")
            return nomeResponsavel2
        elif verResponsavel == 'não' or verResponsavel == 'nao':
            return None
        else:
            print("Opção inválida")
            responsavel2()