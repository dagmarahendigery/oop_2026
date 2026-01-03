# Klasa = Szablon, Przepis
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
        # adam.imie = "Adam"
        # ewa.imie = "Ewa"

    # Metoda
    # Możność (możliwość), zdolność, umiejętność
    def przedstaw_sie(self):
        print(f"Dzień dobry, mam na imię {self.imie} i jestem ", end="")
        if self.plec=="M":
            print("mężczyzną")
        else:
            print("kobietą")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

# Powstawanie obiektu (Instancji klasy Czlowiek)
# (Gotowanie z przepisu)
adam = Czlowiek("Adam", "M")
# a = 4 # a = int(4)
ewa = Czlowiek("Ewa", "K")

adam.przedstaw_sie()
ewa.przedstaw(adam)