class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def verSaldo(self):
        print(f"Boa noite {self.titular}! Seu saldo é R$ {self.saldo}")

    def depositar(self):
        valor = float(input("Digite o valor que você quer depositar: "))
        self.saldo += valor
        print(f"Seu saldo é R$: {self.saldo}")

    def sacar(self):
        valorSacar = float(input("Digite o valor que você quer sacar: "))
        self.saldo -= valorSacar
        print(f'O valor sacado foi de R$: {valorSacar}, seu saldo atual é de R$ {self.saldo}')



saldo1 = ContaBancaria("Miguel", 200)

saldo1.verSaldo()
saldo1.depositar()
saldo1.sacar()