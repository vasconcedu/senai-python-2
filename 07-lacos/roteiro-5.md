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

## Exercício 2

Escreva um programa chamado `adivinhacao.py`, que implementa um jogo da adivinhação de números.

O seu programa deve gerar um número pseudoaleatório de 1 a 100 _**(o professor vai explicar como fazer essa parte!)**_, e o jogador vai ter 10 tentativas para adivinhar qual foi o número que o programa gerou.

Após cada tentativa:

- Se o jogador tiver acertado o número, o programa deve informar que o jogador ganhou e encerrar;
- Se o jogador tiver errado o número, mas ainda tiver tentativas restantes, o programa deve informar ao jogador que ele errou e quantas tentativas restantes ele ainda tem. O programa deve informar, ainda, se o palpite foi muito alto ou se foi muito baixo e solicitar que o jogador tente novamente;
- Já se o jogador tiver errado o número e não tiver mais tentativas restantes, o programa deve informar ao jogador que ele perdeu e encerrar.

