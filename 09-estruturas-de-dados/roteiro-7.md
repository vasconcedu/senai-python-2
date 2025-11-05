# 💻 Roteiro 7

## Exercício 1

O arquivo `ex-1.py` contém a base de um programa de cadastro de alunos.

Revise o código e execute o programa uma vez para testá-lo e entender o seu funcionamento.

Em seguida, modifique o programa para implementar as operações de cadastro, utilizando as operações básicas de listas:

1. Se o usuário selecionar a operação `1`, o programa deve pedir que o usuario digite o nome de um novo aluno a ser adicionado à lista de cadastro e, em seguida, adicionar o novo aluno à lista;
2. Se o usuário selecionar a operação `2`, o programa deve pedir o índice de um aluno e, em seguida, exibir o nome do aluno cujo índice na lista de cadastro corresponde ao índice fornecido pelo usuário;
    
    > 🚨 ATENÇÃO: se o índice fornecido pelo usuário for inválido, o programa deve mostrar uma mensagem de erro na tela!

3. Se o usuário selecionar a operação `3`, o programa deve pedir o nome de um aluno e, em seguida, remover esse aluno da lista de cadastro;

    > 🚨 ATENÇÃO: se o nome fornecido pelo usuário não existir na lista de cadastro, o programa deve mostrar essa informação na tela!

    > 💡 Dica: você pode usar `range(0, len(alunos))` em um laço `for` para iterar sobre a lista de cadastro com base nos índices dos alunos.

4. Se o usuário selecionar a operação `4`, o programa deve exibir a lista completa de alunos cadastrados;
5. Se o usuário selecionar a operação `5`, o programa deve remover todos os alunos da lista.

## Exercício 2 

Modifique as operações do programa do exercício 1 para que o cadastro de um aluno contenha, além do nome do aluno, uma lista de notas.

Utilize uma estrutura de dicionário para realizar o cadastro, de forma que os pares chave-valor do dicionário sejam compostos por:

- Chave: o nome do aluno; e
- Valor: a lista de notas do aluno.

Ou seja, o seu dicionário deve ter um formato parecido com o seguinte: 

```
{
    "Aristoteles": [10.0, 10.0, 10.0],
    "Platao": [10.0, 10.0, 10.0], 
    "Arquimedes": [10.0, 10.0, 10.0]
}
```

As operações de `1` a `5` devem ser modificadas conforme as especificações abaixo: 

1. A operação `1` deve cadastrar um novo aluno no dicionário e inicializar o seu cadastro com uma lista de notas vazia;
2. A operação `2` deve exibir, além do nome do aluno, a sua respectiva lista de notas;
3. A operação `3` deve ter o mesmo comportamento do programa do exercício 1;
4. A operação `4` deve ter o mesmo comportamento do programa do exercício 1, mas deve mostrar, além dos nomes dos alunos, as suas respectivas listas de notas;
5. A operação `5` deve ter o mesmo comportamento do programa do exercício 1;
6. A operação `6` deve passar a ser a operação `7`.

Implemente, ainda, uma nova operação `6`, cujo comportamento é o seguinte: se o usuário selecionar a operação `6`, o programa deve pedir o nome de um aluno e, em seguida, uma nota. O programa deve adicionar a nota à lista de notas do aluno.

> 🚨 ATENÇÃO: se o nome fornecido pelo usuário não existir na lista de cadastro, o programa deve mostrar essa informação na tela!
