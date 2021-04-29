import random


class Karta:
    def __init__(self,wartosc,znak):
        self.wartosc = wartosc
        self.znak = znak 

class Talia:
    def __init__(self):
        self.talia = []
        self.tworzenie()
    def tworzenie(self):
        for i in ["Pik","Kier","Trefl","Karo"]:
            for j in range(1,14):
                self.talia.append(Karta(j,i))
    def pokaztalie(self):
        for i in self.talia:
            print(f"{i.wartosc} {i.znak}")

class Gracz:
    def __init__(self,name):
        self.name = name
        self.czekanie = 0
        self.karty = []
    def __repr__(self):
        j = 1
        print(f"Twoje karty:")
        for i in self.karty:
            print(f"{j}.Wartość: {i.wartosc} znak: {i.znak}")
            j+=1
    def wybraniekart(self,talia):
        for i in range (5):
            self.karty.append(talia.talia[random.randint(0,len(talia.talia)-1)])
    def usunkarte(self,karta):
        self.karty.remove(karta)
    def dobierzkarte(self,talia):
        self.karty.append(talia.talia[random.randint(0,len(talia.talia))-1])

class Stol:
    def __init__(self,talia):
        self.karta = talia.talia[random.randint(0,len(talia.talia))-1]
    def dodawanie(self,gracz,ilosc,talia):
        jest = [False,0]
        for i in gracz.karty:
            if i.wartosc == self.karta.wartosc or (i.znak == self.karta.znak and (i.wartosc == 3 or i.wartosc == 2)):
                jest = [True,i]
        if jest[0]==False:
            print(f"Niesety nie miałeś żadnej karty by moc to odbic, musisz ciagnac {ilosc} kart")
            for i in range(ilosc):
                gracz.dobierzkarte(talia)
                return 0
        else:
            print("Masz kartę by odbić do następnego gracza")
            self.karta = jest[1]
            gracz.usunkarte(jest[1])
            return ilosc+ jest[1].wartosc
    def blokada(self,gracz,czekac):
        jest = [False,0]
        for i in gracz.karty:
            if i.wartosc == self.karta.wartosc:
                jest = [True,i]
        if jest[0]==False:
            print("Nie masz karty by móc odbić")
            gracz.czekanie = czekac
        else:
            print("Masz kartę by odbić do następnego gracza")
            self.karta = jest[1]
            gracz.usunkarte(jest[1])
            return czekac+1
    def zmianakolor(self):
        self.karta.znak = input("Na jaki kolor chcesz zmienić? Pik,Kier,Trefl,Karo ")
    def wybierzkarte(self,gracz,talia):
        if input("Czy chcesz ciągnąć? ") == "tak":
            gracz.dobierzkarte(talia)
            return None
        while True:
            wybrana = int(input("Którą kartę chcesz dać? "))
            if gracz.karty[wybrana-1].znak == self.karta.znak or gracz.karty[wybrana-1].wartosc == self.karta.wartosc or gracz.karty[wybrana-1].wartosc == 12 or self.karta.wartosc ==12:   
                return gracz.karty[wybrana-1]
            print("Wybrałeś kartę którą nie możesz dać")
    def makao(self,gracze,talia):
        kartydociagniecia = 0
        czekanie = 0
        print("Witamy w grze Mako\nOto gracze którzy biorą udział w grze:")
        for i in gracze:
            print(i.name)
        while True:
            for i in gracze:
                print(f"Kolej {i.name}")
                if i.czekanie >0:
                    print("Wciąż musisz czekać")
                i.__repr__()
                print(f"Karta na stole {self.karta.znak} {self.karta.wartosc}")
                if (self.karta.wartosc == 2 or self.karta.wartosc == 3) and kartydociagniecia>0:
                    kartydociagniecia =self.dodawanie(i,kartydociagniecia,talia)
                elif self.karta.wartosc == 4 and czekanie>0:
                    czekac = self.blokada(i,czakac)
                else:
                    wybrana = self.wybierzkarte(i,talia)
                    if wybrana == None:
                        continue
                    else:
                        self.karta = wybrana
                    if self.karta.wartosc == 2 or self.karta.wartosc == 3:
                        kartydociagniecia+=self.karta.wartosc
                    elif self.karta.wartosc == 4:
                        czekanie+=1
                    elif self.karta.wartosc == 1:
                        self.zmianakolor()
                    i.usunkarte(self.karta)
                if len(i.karty) == 0:
                    return f"Gracz {i.name} wygrał"


talia = Talia()
talia.pokaztalie()
stol = Stol(talia)
gracze = []
ilegraaczy = int(input("Ile graczy gra? "))
for i in range (ilegraaczy):
    gracze.append(Gracz(input("Podaj nazwe gracza: ")))
    gracze[i].wybraniekart(talia)

print(stol.makao(gracze,talia))
'''gracze=[Gracz("Nom"),Gracz("Lool")]
gracze[0].wybraniekart(talia)
gracze[0].__repr__()'''

'''
Niepełne Makao
Zasady:
1.2 i 3 bierzesz karty 
2. 4 blokuje następnego gracza
3. as zmienia kolor 
4. Dama na wszystko wszystko na dame 
5. Pierwsza osoba która ma 0 kart wygrywa 
'''