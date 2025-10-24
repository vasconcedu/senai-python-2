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

## Exercício 2

Neste exercício, iremos resolver um problema clássico da programação: calcular a Sequência de Fibonacci. 

> 🧮 **A Sequência de Fibonacci**
> 
> https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

Escreva uma função chamada `fib(n)`, que recebe como argumento um número inteiro `n` (sendo `n >= 0`) e que calcula o número de Fibonacci do número `n`.

Por exemplo, se a sua função receber o número `7`, ela deve calcular o número de Fibonacci do número `7`, ou `fib(7)`, que na Sequência de Fibonacci corresponde ao número `13`:

```
n:      0 1 2 3 4 5 6 7  ...
fib(n): 0 1 1 2 3 5 8 13 ...
```

> 💡 **Dica 1: como calcular a Sequência de Fibonacci?**
>
> Cada número da Sequência de Fibonacci é calculado pela soma dos dois números que o antecedem na Sequência, ou seja: 
>
> `fib(n) = fib(n-1) + fib(n-2)`
>
> Sendo que os dois primeiros números da Sequência de Fibonacci são:
>
> `fib(0) = 0` e `fib(1) = 1`
>
> Assim, por exemplo, `fib(2)` pode ser calculado fazendo:
>
> `fib(2) = fib(2-1) + fib(2-2)`
>
> `= fib(1) + fib(0)`
>
> `= 1 + 0`
>
> `= 1`
>
> Esse mesmo raciocínio pode ser aplicado para calcular os próximos números da Sequência.

> 💡 **Dica 2: como estruturar a sua função?**
>
> Comece pensando nos casos mais simples: você sabe que `fib(0) = 0`. Logo, o que a sua função deve retornar quando `n == 0`?
>
> Você também sabe que `fib(1) = 1`. Logo, o que a sua função deve retornar quando `n == 1`?
> 
> Por último, pense no caso mais complexo: como calcular os números da sequência de Fibonacci a partir da posição número `2`, ou seja, `fib(n)`, onde `n >= 2`?

## Exercício 3

Utilize a sua função `fib(n)` para escrever um programa que recebe um número `n` do usuário e que mostra toda a Sequência de Fibonacci de `fib(0)` até `fib(n)`.

Use uma função `main()` para receber o número `n` do usuário, efetuar as chamadas à função `fib(n)` e mostrar os valores da Sequência de Fibonacci na tela.

