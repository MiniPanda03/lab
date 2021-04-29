class Zwierze:
    def __init__(self,nazwa,plec,wiek,waga,srodowisko,szybkosc,dzwiek):
        self.nazwa = nazwa
        self.plec = plec 
        self.wiek = wiek
        self.waga = waga
        self.srodowisko = srodowisko
        self.szybkosc = szybkosc
        self.dzwiek = dzwiek
class Kot(Zwierze):
    def __init__(self,nazwa,plec,wiek,waga,srodowisko,szybkosc,dzwiek):
        Zwierze.__init__(self,nazwa,plec,wiek,waga,srodowisko,szybkosc,dzwiek)
        self.gatunek = "Kot"
    def jedzenie (self):
        if self.dzwiek == "miau":
            print("{} jest głodny".format(self.nazwa))
        elif self.dzwiek == "mrrr":
            print("{} jest szczęśliwy".format(self.nazwa))
class Pies(Zwierze):
    def __init__(self,nazwa,plec,wiek,waga,srodowisko,szybkosc,dzwiek):
        Zwierze.__init__(self,nazwa,plec,wiek,waga,srodowisko,szybkosc,dzwiek)
        self.gatunek = "Pies"
    def wyscigi(self,drugiezwierze):
        if self.szybkosc > drugiezwierze.szybkosc:
            print("Twoj {} przescignął {}".format(self.nazwa,drugiezwierze.nazwa))
        else:
            print("Niestety przegranko, {} był za wolny i {} go przescignął".format(self.nazwa,drugiezwierze.nazwa))
srodowiskawodne = ["jezioro","akwarium","wanna","morze","szklanka z woda"]
class Ryba (Zwierze):
    def __init__(self,nazwa,plec,wiek,waga,srodowisko,szybkosc,dzwiek):
        Zwierze.__init__(self,nazwa,plec,wiek,waga,srodowisko,szybkosc,dzwiek)
        self.gatunek = "Ryba"
    def czyzyje(self):
        if self.srodowisko not in srodowiskawodne:
            print("Twoja {} o imieniu {} zmarła z powodu twojej głupoty".format(self.gatunek,self.nazwa))
        else:
            print("{} swietnie się czuje".format(self.nazwa))
koty = Kot("Mruczek","K",10,50,"dom",100,"miau")
koty.jedzenie()
piesel = Pies("Bushi","M",3,20,"dom",70,"hau")
piesel.wyscigi(koty)
rybka = Ryba("Plum","M",1,1,"nope",1,"blup")
rybka.czyzyje()