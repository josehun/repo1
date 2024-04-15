from abc import ABC, abstractmethod
from datetime import date

# Absztrakt Szoba osztály
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def get_ar(self):
        pass

# EgyágyasSzoba osztály
class EgyagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar

# KétágyasSzoba osztály
class KetagyasSzoba(Szoba):
    def get_ar(self):
        return self.ar
    
# Foglalás osztály
class Foglalas:
    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum

# Szálloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        if datum <= date.today():
            return "Érvénytelen dátum"
        if szobaszam not in [szoba.szobaszam for szoba in self.szobak]:
            return f"Nincs ilyen szobaszám, kérjük az alábbi szobákból válasszon: {self.elerheto_szobak()}"
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                return "A szoba ezen a napon már foglalt"
        self.foglalasok.append(Foglalas(szobaszam, datum))
        return f"Foglalás rögzítve. Ár: {next(szoba for szoba in self.szobak if szoba.szobaszam == szobaszam).get_ar()}"

    def elerheto_szobak(self):
        return ', '.join(f"{szoba.szobaszam} - {'egyágyas' if isinstance(szoba, EgyagyasSzoba) else 'kétágyas'} {szoba.get_ar()}" for szoba in self.szobak)

    def foglalas_lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Foglalás lemondva"
        return "Nem található ilyen foglalás"

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincsenek foglalások"
        return '\n'.join(f"Szobaszám: {foglalas.szobaszam}, Dátum: {foglalas.datum}" for foglalas in self.foglalasok)

# Felhasználói interakció
def felhasznalo_interakcio(szalloda):
    print(f"Üdvözöljük a {szalloda.nev} szállodában!")
    while True:
        print("\nVálasszon az alábbi opciók közül:")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Kérjük, adja meg a választott opció számát: ")
        
        if valasztas == '1':
            szobaszam = int(input("Adja meg a szobaszámot: "))
            ev, honap, nap = map(int, input("Adja meg a foglalás dátumát (év hónap nap): ").split())
            datum = date(ev, honap, nap)
            print(szalloda.foglalas(szobaszam, datum))
        elif valasztas == '2':
            szobaszam = int(input("Adja meg a szobaszámot: "))
            ev, honap, nap = map(int, input("Adja meg a lemondás dátumát (év hónap nap): ").split())
            datum = date(ev, honap, nap)
            print(szalloda.foglalas_lemondas(szobaszam, datum))
        elif valasztas == '3':
            print("Foglalások listája:")
            print(szalloda.foglalasok_listazasa())
        elif valasztas == '4':
            print("Köszönjük, hogy minket választott!")
            break
        else:
            print("Érvénytelen választás. Kérjük, próbálja újra.")

# Példányosítás és tesztelés
szalloda = Szalloda("Példa Szálloda")
szalloda.szoba_hozzaadas(EgyagyasSzoba(10000, 101))
szalloda.szoba_hozzaadas(KetagyasSzoba(15000, 102))
szalloda.szoba_hozzaadas(EgyagyasSzoba(10000, 103))

# Tesztadatok betöltése
szalloda.foglalas(101, date(2024, 5, 20))
szalloda.foglalas(102, date(2024, 6, 15))
szalloda.foglalas(103, date(2024, 7, 10))
szalloda.foglalas(101, date(2024, 8, 16))
szalloda.foglalas(102, date(2024, 9, 25))

# Felhasználói interakció elindítása
felhasznalo_interakcio(szalloda)
