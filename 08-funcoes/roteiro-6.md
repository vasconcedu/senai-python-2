# 💻 Roteiro 6

## Exercício 1

Escreva um programa que recebe como entradas um número decimal qualquer _(o professor vai explicar como fazer essa parte!)_ e uma operação aritmética (i.e. os caracteres `+`, `-`, `*` ou `/`).

O seu programa deve exibir a tabuada (de 0 a 10) correspondente ao número e à operação lidos. Por exemplo, se o seu programa receber o número `7.0` e a operação `+`, ele deve mostrar na tela:

```
7.0 + 0 = 7.0
7.0 + 1 = 8.0
7.0 + 2 = 9.0
7.0 + 3 = 10.0
7.0 + 4 = 11.0
7.0 + 5 = 12.0
7.0 + 6 = 13.0
7.0 + 7 = 14.0
7.0 + 8 = 15.0
7.0 + 9 = 16.0
7.0 + 10 = 17.0
```

Implemente uma única função chamada `tabuada(n, op)`, que calcula e mostra a tabuada do número `n` para uma operação `op` fornecida. A sua função deve lidar com os quatro tipos de operações aritméticas. 

Em seguida, use uma função `main()` para receber do usuário o número e a operação aritmética desejados e, em seguida, chamar a função `tabuada(n, op)`, passando o número e a operação recebidos.

