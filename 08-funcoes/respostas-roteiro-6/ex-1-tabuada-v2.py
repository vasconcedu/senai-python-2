def linha_tabuada(n, op, i, res):
    return f"{n} {op} {i} = {res}\n"

def tabuada(n, op):
    saida = ""
    for i in range(11):
        if op == "+":
            saida += linha_tabuada(n, op, i, n + i)
        elif op == "-":
            saida += linha_tabuada(n, op, i, n - i)
        elif op == "*":
            saida += linha_tabuada(n, op, i, n * i)
        elif op == "/":
            resultado = n / i if i != 0 else "Indefinido"
            saida += linha_tabuada(n, op, i, resultado)
    return saida 

def main():
    numero = float(input("Numero: "))
    operacao = input("Operacao: ")
    print(tabuada(numero, operacao))

main()
