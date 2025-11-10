alunos = {}

while(True):
    operacao = int(input("\n==========\n\nSelecione a operacao desejada:\n\n\t1: adicionar aluno\n\t2: exibir aluno\n\t3: remover aluno\n\t4: exibir lista de alunos\n\t5: remover todos os alunos\n\t6: cadastrar nota\n\t7: sair\n\nOperacao> "))
    
    if operacao == 1:
        nome = input("Nome do aluno> ")
        alunos[nome] = []
    elif operacao == 2:
        nome = input("Nome do aluno> ")

        # Implementacao com for e flag de controle
        aluno_encontrado = False
        for ch, _ in alunos.items():
            if ch == nome:
                print(f"{nome}: {alunos[nome]}")
                aluno_encontrado = True 
                break
        if not aluno_encontrado:
            print("Erro: aluno nao encontrado!")

        # Implementacao com in
        # if nome in alunos:
        #     print(f"{nome}: {alunos[nome]}")
        # else:
        #     print("Erro: aluno nao encontrado!")

        # Implementacao com for/else
        # for ch, _ in alunos.items():
        #     if ch == nome:
        #         print(f"{nome}: {alunos[nome]}")
        #         aluno_encontrado = True 
        #         break
        # else:
        #     print("Erro: aluno nao encontrado!")
        
    elif operacao == 3:
        nome = input("Nome do aluno> ")

        # Implementacao com for e flag de controle
        aluno_encontrado = False
        for ch, _ in alunos.items():
            if ch == nome:
                del alunos[nome]
                aluno_encontrado = True 
                break
        if not aluno_encontrado:
            print("Erro: aluno nao encontrado!")

        # Implementacao com for e len
        # len_inicial = len(alunos)
        # for ch, _ in alunos.items():
        #     if ch == nome:
        #         del alunos[nome]
        #         break
        # if len(alunos) == len_inicial:
        #     print("Erro: aluno nao encontrado!")
        
    elif operacao == 4:
        for ch, val in alunos.items():
            print(f"{ch}: {val}")
    elif operacao == 5:
        alunos = {}
    elif operacao == 6:
        nome = input("Nome do aluno> ")
        if nome in alunos: 
            nota = float(input("Nota> "))
            if 0.0 <= nota <= 10.0:
                alunos[nome].append(nota)
            else:
                print("Erro: nota invalida!")
        else:
            print("Erro: aluno nao encontrado!")
    elif operacao == 7:
        exit()
    else:
        print("Erro: operacao desconhecida!")
