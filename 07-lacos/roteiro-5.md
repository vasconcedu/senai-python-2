# 💻 Roteiro 5

## Exercício 1

Escreva um programa chamado `caixa.py`, que simula o comportamento de um caixa eletrônico. 

Suponha que o saldo inicial do usuário é `0`. O seu programa deve pedir uma entrada ao usuário, sendo que as 4 entradas possíveis são os comandos:

- `sair`;
- `saldo`;
- `deposito`; e
- `saque`.

Caso o usuário forneça o comando `sair`, o seu programa deve encerrar.

Caso o usuário forneça o comando `saldo`, o seu programa deve mostrar o saldo do usuário. Depois, o programa deve solicitar um novo comando.

Caso o usuário forneça o comando `deposito`, o seu programa deve simular o fluxo de um depósito no caixa eletrônico, solicitando o valor a ser depositado e, em seguida, adicionando o valor de depósito fornecido ao saldo do usuário. Depois, o programa deve solicitar um novo comando.

Caso o usuário forneça o comando `saque`, o seu programa deve simular o fluxo de um saque no caixa eletrônico, solicitando o valor a ser sacado e, em seguida, subtraindo o valor de saque fornecido do saldo do usuário. Depois, o programa deve solicitar um novo comando.

Caso o usuário digite qualquer outra entrada além dos 4 comandos acima, o seu programa deve informar que a entrada digitada é inválida. 

> Obs.: para os comandos de `deposito` e `saque`, lembre-se de verificar se os valores fornecidos pelo usuário são válidos (i.e. se são maiores do que `0`).

