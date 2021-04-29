class Ksiazka:
    def __init__ (self,tytul,autor,cena,rodzaj,opis,ileStron):
        self.tytul = tytul
        self.autor = autor 
        self.cena = cena
        self.rodzaj = rodzaj
        self.opis = opis
        self.ileStron = ileStron
    def zakup(self,pieniadze):
        if pieniadze>self.cena:
            return "Zakupiłeś książke {} życze udanego czytania :) ".format(self.tytul)
        return "Nie masz wystarczającej ilości pieniędzy, brakuje ci {}".format(self.cena-pieniadze)
    def czytaj(self,szykosc,czas):
        if szybkosc*czas>self.ileStron:
            return "Przeczytałeś całą książke"
        przeczytane = szykosc*czas
        return "Czytałeś ale nie dokończyłeś jeszcze książki, zostało ci {} i skonczyłeśna stronie {}".format(self.ileStron-przeczytane,przeczytane)
    def zmiananopisu(self):
        self.opis = input("Opisz książke: ")
    def sortowanie(tab):
        tab.sort()
        return "Książki zostały posortowane"
    def __repr__(self):
        return "Tytuł: {}\nAutor: {}\nRodzaj: {}\nIlość stron: {}\nOpis: {}\n Cena:{}".format(self.tytul,self.autor,self.rodzaj,self.ileStron,self.opis,self.cena)

ksiazka = [Ksiazka("Qwer","Sasdasd Ddsacsc",100,"asd","jndsajndkjsanjs",150)]
print(ksiazka.zakup(50))
print(ksiazka.czytaj(10,3))
print(ksiazka.zmiananopisu())

