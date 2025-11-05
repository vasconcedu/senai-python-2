alunos = [] 

while(True):
    operacao = int(input("\n==========\n\nSelecione a operacao desejada:\n\n\t1: adicionar aluno\n\t2: exibir aluno\n\t3: remover aluno\n\t4: exibir lista de alunos\n\t5: remover todos os alunos\n\t6: sair\n\nOperacao> "))
    
    if operacao == 1:
        nome = input("Nome do aluno> ")
        alunos.append(nome)
    elif operacao == 2:
        indice = int(input("Indice> "))
        if indice >= 0 and indice < len(alunos):
            print(alunos[indice])
        else:
            print("Erro: indice invalido!")
    elif operacao == 3:
        nome = input("Digite o nome do aluno a remover> ")
        aluno_removido = False
        for i in range(0, len(alunos)):
            if alunos[i] == nome:
                del alunos[i]
                aluno_removido = True
                print("Aluno removido com sucesso!")
                break
        if not aluno_removido:
            print("Erro: aluno nao cadastrado!")
    elif operacao == 4:
        for i in range(0, len(alunos)):
            print(f"{i}: {alunos[i]}")
    elif operacao == 5:
        alunos = []
    elif operacao == 6:
        exit()
    else:
        print("Erro: operacao desconhecida!")
