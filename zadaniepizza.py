# ==========================================
# Zadanie: Pizza + alergeny + opłacalność
# ==========================================
# USER STORIES:
# 1. Jako konsument pizzy chcę wiedzieć,
#    czy pizza zawiera alergen
# 2. Jako konsument pizzy chcę policzyć
#    opłacalność pizzy, aby porównać pizze
# ==========================================


class Pizza:
    # Konstruktor klasy Pizza
    def __init__(self, nazwa, skladniki, cena, srednica):
        self.nazwa = nazwa              # nazwa pizzy
        self.skladniki = skladniki      # lista składników
        self.cena = cena                # cena w zł
        self.srednica = srednica        # średnica w cm

    # Sprawdzenie czy pizza zawiera alergen
    def czy_zawiera_alergen(self, alergen):
        return alergen.lower() in [s.lower() for s in self.skladniki]

    # Obliczenie opłacalności pizzy
    # im mniejsza wartość -> tym lepsza opłacalność
    def oplacalnosc(self):
        return self.cena / self.srednica

    # Wyświetlenie informacji o pizzy
    def pokaz_info(self):
        print(f"🍕 Pizza: {self.nazwa}")
        print(f"Składniki: {', '.join(self.skladniki)}")
        print(f"Cena: {self.cena} zł")
        print(f"Średnica: {self.srednica} cm")
        print(f"Opłacalność: {self.oplacalnosc():.2f} zł/cm")
        print("-" * 40)


# ==========================
# CZĘŚĆ URUCHAMIALNA PROGRAMU
# ==========================

pizza1 = Pizza(
    "Margherita",
    ["ser", "pomidor", "bazylia"],
    30,
    32
)

pizza2 = Pizza(
    "Pepperoni",
    ["ser", "pomidor", "pepperoni", "gluten"],
    36,
    40
)

# Wyświetlenie informacji
pizza1.pokaz_info()
pizza2.pokaz_info()

# Sprawdzenie alergenu
alergen = "gluten"

print(f"Czy {pizza1.nazwa} zawiera {alergen}? "
      f"{pizza1.czy_zawiera_alergen(alergen)}")

print(f"Czy {pizza2.nazwa} zawiera {alergen}? "
      f"{pizza2.czy_zawiera_alergen(alergen)}")

# Porównanie opłacalności
if pizza1.oplacalnosc() < pizza2.oplacalnosc():
    print(f"✅ Bardziej opłacalna pizza: {pizza1.nazwa}")
else:
    print(f"✅ Bardziej opłacalna pizza: {pizza2.nazwa}")
