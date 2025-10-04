idade = int(input("Qual eh a sua idade? "))

if 0 <= idade <= 12:
    print("Crianca")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade invalida!")
