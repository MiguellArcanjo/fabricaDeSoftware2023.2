class FormaGeometrica():

    def calcularArea(self):
        return 'TESTando'


class Retangulo(FormaGeometrica):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calcularArea(self):
        return self.b * self.h
    
class Circulo(FormaGeometrica):
    def __init__(self, r):
        self.r = r

    def calcularArea(self):
        pi = 3.14

        return pi * self.r ** 2     # 78,5 ou 78,75
    

retangulo = Retangulo(2, 5)
circulo = Circulo(5)

print(retangulo.calcularArea())
print(circulo.calcularArea())
