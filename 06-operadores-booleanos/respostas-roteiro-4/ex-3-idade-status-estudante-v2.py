idade = int(input("Qual eh a sua idade? "))
estudante = input("Voce eh estudante? (sim/nao) ")

rotulo_idade = None
rotulo_estudante = None

if 0 <= idade <= 12:
    rotulo_idade = "Crianca"
elif 13 <= idade <= 17:
    rotulo_idade = "Adolescente"
elif 18 <= idade <= 59:
    rotulo_idade = "Adulto"
elif idade >= 60:
    rotulo_idade = "Idoso"

if estudante == "sim":
    rotulo_estudante = ""
elif estudante == "nao":
    rotulo_estudante = " nao"

if rotulo_idade == None or rotulo_estudante == None:
    print("Entrada invalida")
else:
    print(f"{rotulo_idade}{rotulo_estudante} estudante")
