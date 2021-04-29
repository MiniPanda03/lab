class Hotel:
    def __init__(self,nazwa,pietra,pokoj):
        self.nazwa = nazwa
        self.pietra = pietra
        self.pokoj = pokoj
        self.hotel = []
        self.tworzniehotelu()
    def tworzniehotelu(self):
        numer = 1
        for i in range (self.pietra):
            self.hotel.append([])
            for j in range (self.pokoj):
                self.hotel[i].append(NrPokoju(self.nazwa,i,numer))
                numer+=1
    def wyswietlhotel(self):
        print(f"Witamy w hotelu {self.nazwa}")
        for i in range(len(self.hotel)-1,-1,-1):
            for j in range(len(self.hotel[i])):
                if self.hotel[i][j].pokoj <10:
                    odprow = "  "
                else:
                    odprow = " "
                print(f"|{self.hotel[i][j].pokoj}|",end=odprow)
            print("")
        for i in range(self.pokoj):
            print("-----",end="")
    def wynamijpokoj(self,osoba,wybrany):
        for i in self.hotel:
            for j in i:
                if j.pokoj == wybrany:
                    j.wynajety = True
                    j.nazwisko = osoba.nazwisko
                    return f"Pokoj {j.pokoj} zostal wynajety przez {osoba.nazwisko}"
    def wynajmijwielepokoji(self,osoba,ile,wybrane):
        wolne = self.ilewolnych()
        if ile > len(wolne):
            return f"Nie mozna zamowic tyle pokoji, jest tylko {self.ilewolnych()}"
        if wybrane == True:
            for i in range (ile):
                while True:
                    wybrany = int(input("Wybierz: "))
                    if wybrany in wolne:
                        print(self.wynamijpokoj(osoba,wybrany))
                        break
        else:
            for i in range (ile):
                self.wynamijpokoj(osoba,wolne[i])
                
    def czymoznaobok(self,ile):
        pierwszy = ''
        licznik = 0
        for i in self.hotel:
            for j in i:
                if j.wynajety == False and licznik == 0:
                    pierwszy = j
                    licznik+=1
                elif j.wynajety == False:
                    licznik+=1
                    if licznik == ile:
                        return f"Od pokoju nr {pierwszy.pokoj} mozna wynjac {ile} pokoji obok siebie"
                else:
                    licznik = 0 
                    pierwszy = ''
        return null

    def ilewolnych(self):
        wolne = []
        for i in self.hotel:
            for j in i:
                if j.wynajety == False:
                    wolne.append(j.pokoj)
        return wolne
    def sprawdznazwisko(self,osoba):
        wynajete = []
        for i in self.hotel:
            for j in i:
                if j.nazwisko == osoba.nazwisko:
                    wynajete.append(j)
        print(f"{osoba.nazwisko} wynajął pokoje:",end="" )
        for i in wynajete:
            print(i.pokoj,end=",")

class Osoba:
    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class NrPokoju(Hotel):
    def __init__(self,nazwahotelu,pietro,pokoj):
        Hotel.__init__(self,nazwahotelu,pietro,pokoj)
        self.wynajety = False
        self.nazwisko = ""

hotel = Hotel(input("Podaj nazwe hotelu: "),int(input("Podaj ilosc pieter: ")),int(input("Podaj ilosc pokoji na pietro: ")))
goscie = [Osoba("sas","dsc")]
hotel.wynajmijwielepokoji(goscie[0],1,False)

while True:
    hotel.wyswietlhotel()
    print("\nOpcje:\n1.Sprawdz ile jes wolnych pokoji \n2.Zarezerwuj pokoj\n3.Spradz jakie pokoje sa zarezerwowoane na nazwisko \n4.Sprawdz czy mozna iles pokoji zarezerwowac przy sobie \n5.Stworz nowego goscia")
    opcja = int(input("Ktora opcje wybierasz? "))
    if opcja == 1 :
        print(len(hotel.ilewolnych()))
    elif opcja == 2:
        print("Dostepni goscie:")
        for i in range(len(goscie)):
            print(f"{i+1}.{goscie[i].imie} {goscie[i].nazwisko}")
        hotel.wynajmijwielepokoji(goscie[int(input("Kto wynajmuje pokoj/e?: (podaj numer) "))-1],int(input("Jaka ilosc pokoji chcesz wynajac? ")),bool(input("Czy chcesz wybrac samemu pokoj? True/Fasle ")))
    elif opcja == 3:
        print("Dostepni goscie:")
        for i in range(len(goscie)):
            print(f"{i+1}.{goscie[i].imie} {goscie[i].nazwisko}")
        hotel.sprawdznazwisko(goscie[int(input("Kogo sprawdzic? "))-1])
    elif opcja == 4:
        print(hotel.czymoznaobok(int(input("Ile pokoji? "))))
    elif opcja == 5:
        goscie.append(Osoba(input("Podaj imie: "),input("Podaj nazwisko: ")))
        print("Stworzono nowego goscia")
    else:
        print("Podano niepoprawna opcje")


    