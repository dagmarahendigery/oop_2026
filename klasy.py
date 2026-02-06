import random

class Czlowiek:
    # Istota
    # atrybuty KLASY
    # (Cechy wspólne KAŻDEGO Czlowieka)
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec): # atrybuty OBIEKTU (składniki potrawy)
        # (Cechy KONKRETNEJ OSOBY)
        # Konstruktor
        # Akt Istnienia
        # Gotowanie
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec
    def zrob_dziecko(self, other):
        if isinstance(other, Czlowiek) and self.plec != other.plec:
            return Dziecko(None, random.choice(("M", "K")))

    def przedstaw_sie(self):
        print(f"Dzień dobry, mam na imię {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("mężczyzną")
        else:
            print("kobietą")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

class Dziecko(Czlowiek):
    def __init__(self, imie, plec):
        print("powstaje dziecko")
        super().__init__(imie, plec)

    def baw_sie(self):
        print("Ale zabawa, juhuu!!!!")

    def przedstaw_sie(self, osoba):
        print(f"Ceść, jestem {self.imie} i jestem ", end="")
        if self.plec=="M":
            print("chłopcem")
        else:
            print("dziewczynką")

# Powstawanie obiektu (Instancji klasy Czlowiek)
# (Gotowanie z przepisu)
adam = Czlowiek("Adam", "M")
# a = 4 # a = int(4)
ewa = Czlowiek("Ewa", "K")
kain = Dziecko("Kain", "M")
ewa.przedstaw_sie()
kain.baw_sie()

Adam = Czlowiek (imie="Adam", plec="M")
Ewa = Czlowiek (imie="Ewa", plec="K")
