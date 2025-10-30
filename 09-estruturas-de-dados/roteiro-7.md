# 💻 Roteiro 7

## Exercício 1

O arquivo `ex-1.py` contém a base de um programa de cadastro de alunos.

Revise o código e execute o programa uma vez para testá-lo e entender o seu funcionamento.

Em seguida, modifique o programa para implementar as operações de cadastro, utilizando as operações básicas de listas:

1. Se o usuário selecionar a operação `1`, o programa deve pedir que o usuario digite o nome de um novo aluno a ser adicionado à lista de cadastro e, em seguida, adicionar o novo aluno à lista;
2. Se o usuário selecionar a operação `2`, o programa deve pedir o índice de um aluno e, em seguida, exibir o nome do aluno cujo índice na lista de cadastro corresponde ao índice fornecido pelo usuário;
    
    > 🚨 Atenção: se o índice fornecido pelo usuário for inválido, o programa deve mostrar uma mensagem de erro na tela!

3. Se o usuário selecionar a operação `3`, o programa deve pedir o nome de um aluno e, em seguida, remover esse aluno da lista de cadastro;

    > 🚨 ATENÇÃO: se o nome fornecido pelo usuário não existir na lista de cadastro, o programa deve mostrar essa informação na tela!

    > 💡 Dica: você pode usar `range(0, len(alunos))` em um laço `for` para iterar sobre a listade cadastro com base nos índices dos alunos.

4. Se o usuário selecionar a operação `4`, o programa deve exibir a lista completa de alunos cadastrados;
5. Se o usuário selecionar a operação `5`, o programa deve remover todos os alunos da lista.
