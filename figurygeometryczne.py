class FiguraGeometryczna:
    def __init__(self):
        pass

    def pole(self):
        pass

    def obwod(self):
        pass


class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

class Kwadrat(FiguraGeometryczna):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def obwod(self):
        return 4 * self.a

    def pole(self):
        return self.a ** 2


    def obwodprostokata(self):
        return 2 * (self.a + self.b)

    def poleprostokata(self):
        return self.a * self.b

    def polekwadratu(self):
        return self.a * self.a

    def obwodkwadratu(self):
        return 4 * self.a


a = 5
b = 9

p = Prostokat(a, b)
print("Obwód prostokąta:", p.obwod())
print("Pole prostokąta:", p.pole())

k = Kwadrat(a)
print("Obwód kwadratu:", k.obwod())
print("Pole kwadratu:", k.pole())
