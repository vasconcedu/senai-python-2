idade = int(input("Qual eh a sua idade? "))
estudante = input("Voce eh estudante? (sim/nao) ")

if 0 <= idade <= 12 and estudante == "sim":
    print("Crianca estudante")
elif 0 <= idade <= 12 and estudante == "nao":
    print("Crianca nao estudante")
elif 13 <= idade <= 17 and estudante == "sim":
    print("Adolescente estudante")
elif 13 <= idade <= 17 and estudante == "nao":
    print("Adolescente nao estudante")
elif 18 <= idade <= 59 and estudante == "sim":
    print("Adulto estudante")
elif 18 <= idade <= 59 and estudante == "nao":
    print("Adulto nao estudante")
elif idade >= 60 and estudante == "sim":
    print("Idoso estudante")
elif idade >= 60 and estudante == "nao":
    print("Idoso nao estudante")
else:
    print("Entrada invalida")
