velocidade = int(input("Digite a velocidade do carro: "))
multa = velocidade - 80

if velocidade > 80:
    calc = multa * 7
    print("Sua multa é de R$: ", calc)

else:
    print("Você não foi mutado")

