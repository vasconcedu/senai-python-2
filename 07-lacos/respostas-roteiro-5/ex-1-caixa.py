saldo = 0.0

while True:
    comando = input("Digite o comando desejado: ")
    if comando == "sair":
        break
    elif comando == "saldo":
        print(f"Saldo: {saldo}")
    elif comando == "deposito":
        valor_deposito = float(input("Valor a depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
        else:
            print("Valor invalido!")
    elif comando == "saque":
        valor_saque = float(input("Valor a sacar: "))
        if valor_saque > 0:
            if saldo >= valor_saque:
                saldo -= valor_saque
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor invalido!")
