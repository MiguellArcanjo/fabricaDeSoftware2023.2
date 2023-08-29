num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é maior número")

    if num2 < num3:
        print(f"{num2} é o menor número.")
    else:
        print(f"{num3} é o menor número.")

elif num2 > num1 and num2 > num3:
    print(f"{num2} é maior que {num1} e {num3}")

    if num1 < num3:
        print(f"{num1} é o menor número")
    else:
        print(f"{num3} é o menor número")

else:
    print(f"{num3} é maior que {num1} e {num2}")

    if num1 < num2:
        print(f"{num1} é o menor número")
    else:
        print(f"{num3} é o menor número")