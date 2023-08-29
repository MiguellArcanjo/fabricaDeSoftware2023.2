class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"Seu carro da Marca: {self.marca} e de modelo: {self.modelo} do ano {self.ano} ESTA ACELERANDOOOOOOOO")

carro1 = Carro("BMW", "X5", "2023")
carro1.acelerar()