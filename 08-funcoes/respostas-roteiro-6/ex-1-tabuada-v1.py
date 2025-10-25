def tabuada(n, op):
    for i in range(11):
        if op == "+":
            print(f"{n} + {i} = {n + i}")
        elif op == "-":
            print(f"{n} - {i} = {n - i}")
        elif op == "*":
            print(f"{n} * {i} = {n * i}")
        elif op == "/":
            resultado = None
            if i != 0:
                resultado = n / i
            else:
                resultado = "Indefinido"
            print(f"{n} / {i} = {resultado}")

def main():
    numero = float(input("Numero: "))
    operacao = input("Operacao: ")
    tabuada(numero, operacao)

main()
