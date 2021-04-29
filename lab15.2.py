def sortby(napoj):
    return napoj.ocena

class Sklep:
    def __init__(self,nazwa,polka):
        self.nazwa = nazwa
        self.polka = polka
    def sortowaniepoocenie(self,poczym):
        posortowane = self.polka
        posortowane.sort(key=sortby,reverse=True)
        print("Napoje posortowane po ocenie:")
        for i in posortowane:
            print(f"{i.nazwa} {i.ocena}")
    def dodacnopoj(self,napoj):
        self.polka.append(napoj)
    def sprzedawanie(self):
        print("Dostępne napoje: ")
        for i in range(len(self.polka)):
            print(f"{i+1}. {self.polka[i].nazwa}")
        wybrane = int(input("Podaj numer napoju"))
        if self.polka[wybrane-1].kategoria == "piwo":
            if int(input("Podaj swoj wiek: "))<18:
                return "Nie możesz kupić tego napoju"
        return f"Udało ci się kupić {self.polka[wybrane-1].nazwa}"
                
        


class Napoj:
    def __init__(self,nazwa,kategoria,ocena):
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.ocena = ocena
    def wjakichsklepach(self,sklepy):
        dostepne = []
        for i in sklepy:
            for j in i.polka:
                if j.nazwa == self.nazwa:
                    dostepne.append(i.nazwa)
        print("Napój jest dostępny w sklepach:")
        for n in dostepne:
            print(n,end=",")
class Beer(Napoj):
    def __init__(self,nazwa,ocena,procenty):
        super().__init__(nazwa,"piwo",ocena)
        self.procenty = procenty

class Bar(Sklep):
    def __init__(self,nazwa,polka):
        super().__init__(nazwa,polka)

napoje = [Napoj("Cola","cos",4),Napoj("sasa","sd",3),Beer("www",4,5)]
sklep = [Sklep("lsl",napoje),Sklep("sssss",[napoje[2],napoje[1]],),Sklep("qwerty",[napoje[0]])]

sklep[0].sortowaniepoocenie("ocena")
print(sklep[0].sprzedawanie())
napoje[2].wjakichsklepach(sklep)