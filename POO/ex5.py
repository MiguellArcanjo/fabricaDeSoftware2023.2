class Animal():
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        print("Estou fazendo um som")

    def info(self):
        print(f"Sou um {self.nome}")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print("AU AU TO COM FOME")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print("MIAU TO COM FOME")


cachorro = Cachorro("Cachorro")
gato = Gato("Gato")

cachorro.som()
cachorro.info()

gato.som()
gato.info()

