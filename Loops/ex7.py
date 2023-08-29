homens = []
mulheres = []

while True:
    sexo = input("Digite seu sexo, Homem[H] | Mulher [M] | Se quiser sair escreva SAIR: \n").lower()

    if sexo == "sair":
        break

    else:
        if sexo == "m":
            homens.append(sexo)
        else:
            mulheres.append(sexo)
    
print(f"A quantidade de mulheres foi: {len(mulheres)}.")
print(f"A quantidade de Homens foi: {len(homens)}")