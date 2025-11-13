# 💻 Roteiro 8

Realizar modificações em código que foi escrito por terceiros dispondo de pouca documentação é **muito** comum no mercado de tecnologia. Essa tarefa procura simular uma situação como essa, ao mesmo tempo em que exercitamos conceitos de arquivos.

## Introdução

<img src="engenheiro-de-software.png" height="150px">

Você trabalha para a Totalmente Existente Tech Software S.A., uma empresa especializada no desenvolvimento de aplicações. 

O seu chefe pediu que você fizesse algumas modificações na Meus Gastos, uma das aplicações da empresa, que serve para registrar gastos pessoais.

Só tem alguns pequenos probleminhas: até há pouco tempo atrás, você nem sabia da existência dessa aplicação, o engenheiro responsável por ela saiu da empresa há mais de 6 meses, ninguém sabe muito bem como ela funciona e o que é pior: o seu prazo para finalizar as modificações é **hoje,** porque o usuário está esperando e o gerente de relacionamento com o cliente havia prometido as modificações para **ontem.**

## Exercício 1 

Siga as intruções do professor para fazer o setup do ambiente de desenvolvimento.

## Exercício 2

Procure entender a aplicação, respondendo às perguntas abaixo: 

1. O que a aplicação faz? 
2. Quais são as funcionalidades que a aplicação tem?
3. Quantas funções o código tem?
4. De onde vêm os nomes das categorias de gastos que o programa é capaz de cadastrar?
5. Onde o programa armazena os gastos cadastrados?
6. Quais estruturas de dados são utilizadas para armazenar os gastos cadastrados?
7. Qual é o nome da função que realiza o cadastro de um novo gasto?

## Exercício 3

Modifique a Meus Gastos conforme o seu chefe pediu. Ele quer que você implemente as seguintes alterações: 

1. O arquivo de categorias de gastos não deve se chamar mais `categorias_gastos.txt`. O nome desse arquivo agora deve ser apenas `categorias.txt`. Renomeie o arquivo e modifique o programa para refletir esse novo nome;
2. Finalize a implementação da função `limpar_gastos`. Essa função deve permitir que o usuário esvazie a lista de gastos cadastrados.

> 💡 **Dica 1: o que significa esvaziar a lista de gastos?**
> 
> Lembre que a operação de esvaziar a lista de gastos pode ser implementada simplesmente atribuindo a ela uma estrutura de dados vazia.

> 💡 **Dica 2: como implementar a função `limpar_gastos`?**
> 
> A implementação da função `limpar_gastos` é muito parecida com a da função `escrever_gastos`, com a diferença de que, para a função `limpar_gastos`, nós queremos escrever no arquivo uma estrutura de dados vazia.

