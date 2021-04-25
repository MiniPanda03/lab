class Auto:
    def __init__ (self,nazwa,marka,czymPali,wartosc,przebieg,kolor):
        self.nazwa = nazwa
        self.marka = marka
        self.czymPali = czymPali
        self.wartosc = wartosc
        self.przebieg = przebieg 
        self.kolor = kolor
        self.czyWlaczony = False
    def rusz(self,marka):
        return "Twoje auto marki {} przemieszcza się".format(self.marka)
    def cena(self,ubezpieczenie):
        wartosc = float(self.wartosc)+ubezpieczenie
        return "Ostateczna cena za auto wynosi {}".format(wartosc)
    def poruszanie (self,ileprzejechal):
        self.przebieg = float(self.przebieg) + ileprzejechal
        return "Przejechałeś {}, twój przebieg po tej podróży wynosi {}".format(ileprzejechal,self.przebieg)
    def odpal (self):
        if self.czyWlaczony == False:
            self.czyWlaczony = True
            return "Twoje auto zostało odpalone"
        return "Twoje auto było już włączone"
    def cofaj(self):
        return "Cofasz, uważaj"
    def skrec(self,wktorastrone):
        while True:
            if wktorastrone == "prawo" or wktorastrone=="lewo":
                self.przebieg = self.przebieg + 1
                return "Skreciles w {}".format(wktorastrone)
            print("Nieznany kierunek, wpisz ponownie kierunek")
            wktorastrone = input("Podaj kirunek: ")
    def jedzprosto(self,jakdlugo):
        self.przebieg = self.przebieg+jakdlugo
        return "Jedziesz prosto przez {}".format(jakdlugo)
     def __del__(self):
        print(f"Auto {self.nazwa}zostało usunięte")




brumbrum  = []
for i in range(5):
    brumbrum.append(Auto(input("Podaj nazwe"),input("Podaj marka"),input("Podaj czymPali"),input("Podaj wartosc"),input("Podaj przebieg"),input("Podaj kolor")))
print(brumbrum[0].poruszanie(int(input("Jak daleko zajechałeś? (w km)"))))
