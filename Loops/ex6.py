numeros = []

while True:
    num = int(input("Digite um número e caso queira parar digite 0: "))
    
    if num != 0:
        numeros.append(num)
    else:
        break

print(f"a soma de todos os números: {sum(numeros)}.")