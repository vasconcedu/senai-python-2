import random 

# Essa funcao retorna o resultado de um dado de n lados, sendo n um
#   numero inteiro recebido como parametro e que que representa o 
#   numero de lados do dado
def dado(n=6): # O valor default (padrao) de n eh 6!
    return random.randint(1, n)

# Essa funcao usa a funcao dado para implementar o lancamento de uma 
#   moeda, retornando os valores cara ou coroa
def cara_ou_coroa():
    if dado(2) == 1:
        return "cara"
    else:
        return "coroa"

# A funcao main eh a funcao principal do programa
def main():
    contagem_coroa = 0
    contagem_cara = 0
    for i in range(1000000):
        if cara_ou_coroa() == "cara":
            contagem_cara = contagem_cara + 1
        else:
            contagem_coroa = contagem_coroa + 1
    print(f"Contagem de caras: {contagem_cara}")
    print(f"Contagem de coroas: {contagem_coroa}")

main() # Chamada a funcao main!
