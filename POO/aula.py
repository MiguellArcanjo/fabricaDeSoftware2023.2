class Garrafa:
    def __init__(self, tamanho, cor):
        self.tamanho = tamanho
        self.cor = cor

    def __str__(self):
        return f'oi eu sou uma garrafa de tamanhao {self.tamanho} e de cor {self.cor}'

garrafa = Garrafa(100, 'preto')

print(garrafa)
print(garrafa.tamanho)
print(garrafa.cor)