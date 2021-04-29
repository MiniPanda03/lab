class Obywatel:
    def __init__(self,imie,nazwisko,ulica,nr_domu,kod_pocztowy,miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc
    def __repr__(self):
        return "Imie: {}\nNazwisko: {}\nUlica: {}\nNumer domu: {}\nKod pocztowy: {}\nMiejscowość: {}".format(self.imie,self.nazwisko,self.ulica,self.nr_domu,self.kod_pocztowy,self.miejscowosc)

    def drukuj_wizytowke(self):
        plik = open("wizytowka.txt", "w",encoding="utf-8")
        tekst = "------------------------\n{} {}\nul. {} {}\n{} {}\n------------------------".format(self.imie,self.nazwisko,self.ulica,self.nr_domu,self.kod_pocztowy,self.miejscowosc)
        print(tekst)
        plik.write(tekst)
obywatel = Obywatel(input("Podaj imie"),input("Podaj nazwisko"),input("Podaj ulice"),input("Podaj numer domu"),input("Podaj kod pocztowy"),input("Podaj miejscowość"))
print(obywatel.__repr__())
obywatel.drukuj_wizytowke()