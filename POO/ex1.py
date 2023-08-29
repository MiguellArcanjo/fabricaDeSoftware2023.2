class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        return f'Oi, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}'
    
pessoa1 = Pessoa("Miguel", 18, "Programador")

print(pessoa1.saudacao())

arcanjo = Pessoa("Arcanjo", 18, "Programador")

print(arcanjo.saudacao())