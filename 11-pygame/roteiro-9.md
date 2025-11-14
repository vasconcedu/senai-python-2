# 💻 Roteiro 8

## Exercício 1 

Acompanhe a explicação sobre o setup do ambiente e o funcionamento do programa `senai-pong.py`.

## Exercício 2

Responda às perguntas abaixo: 

1. Qual é a linha de código que define o título da janela do jogo?
2. Qual variável é utilizada para tocar o som de beep?
3. Qual função é chamada para tocar o som de beep a partir da variável a que a pergunta anterior se refere?
4. Qual variável define a velocidade de movimento dos retângulos dos jogadores?
5. Quais variáveis são utilizadas para armazenar as pontuações dos jogadores? 
6. Por que o jogo utiliza um laço infinito (i.e. `while True`)?
7. O que a linha de código `tela.fill((0, 0, 0))` faz?
8. O que a linha de código `pygame.draw.rect(tela, (255, 255, 255), retangulo_1)` faz? 
9. Qual é a linha de código que faz o programa encerrar depois que o usuário fecha a janela?
10. O que a linha de código `keys = pygame.key.get_pressed()` faz? 
11. O que a linha de código `bola.center = (bola_centro_x, bola_centro_y)` faz? 

## Exercício 3 

Troque as cores dos elementos do jogo (i.e. tela de fundo, linha de meio-de-campo, retângulos dos jogadores e bola) para cores de sua preferência.

## Exercício 4

Modifique o programa `senai-pong.py` para que o jogo toque um som de vitória (use o arquivo `ponto.mp3`) toda vez que qualquer um dos dois jogadores marcar um ponto.

## Exercício 5

Faça pelo menos mais uma modificação no jogo. Algumas sugestões: 

1. Mudar a velocidade do jogo;
2. Mudar o tamanho da tela do jogo;
3. Mudar a velocidade de algum dos elementos do jogo (i.e. bola, retângulos);
4. Modificar os textos que mostram as pontuações dos jogadores (e.g. mostrar algo como "Player 1: 0 pontos" e "Player 2: 0 pontos" no lugar de apenas "0" e "0");
5. Modificar as posições das pontuações dos jogadores;
6. Modificar as teclas utilizadas para controlar os retângulos dos jogadores;
7. Etc.
