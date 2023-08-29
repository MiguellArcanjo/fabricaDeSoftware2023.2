import operadores as op

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print(f"\nA soma de {num1} e {num2} é: {op.soma(num1, num2)}\n")
print(f"A multiplicação de {num1} e {num2} é: {op.mult(num1, num2)}\n.")
print(f"A subtração de {num1} e {num2} é: {op.sub(num1, num2)}.\n")
print(f"A divisão de {num1} e {num2} é: {op.div(num1, num2)}\n")

