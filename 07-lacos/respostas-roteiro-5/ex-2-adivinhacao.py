import random 

resposta = random.randint(1, 100)

for tentativa in range(1, 11):
    palpite = int(input("Qual eh o seu palpite? "))
    if palpite == resposta:
        print("Voce acertou!")
        break
    elif tentativa < 10:
        s = ""
        if 10 - tentativa > 1:
            s = "s"
        print(f"Voce errou! {10 - tentativa} tentativa{s} restantes...")
        if palpite > resposta:
            print("Palpite muito alto!")
        else:
            print("Palpite muito baixo!")
    else:
        print(f"Voce perdeu! A resposta correta era {resposta}!")
