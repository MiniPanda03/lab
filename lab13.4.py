import random

class Student:
    def __init__(self,imie,nazwisko,nrindexu,plec,kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nrindexu = nrindexu
        self.plec = plec
        self.kierunek = kierunek
    def wyswietldane(self):
        return f"Imie: {self.imie}\nNazwisko: {self.nazwisko}\nNumer indexu: {self.nrindexu}\nPłeć: {self.plec}\nKierunek: {self.kierunek}"
    def kolokfium(self,przedmiot):
        print("Witamy na kolokwium z {}".format(przedmiot))
        if input("Czy przygotowałeś się do niego?")=="Nie":
            print("Niestety nie jesteś przygotowany, ale masz szczęście bo to egzamin zamkniety więc możesz strzelać :) ")
            wynik = random.randint(0,100)
        else:
            print("To super, miejmy nadzieje że dzięki temu uda ci się zdać :)")
            wynik = int(input("W skali od 1 do 10 jak bardzo "))*10
            if wynik <50:
                print("Niestety za mało się nauczyłeś więc tezeba strzelać")
                wynik = wynik+random.randint(0,100-wynik)
        if wynik> 50:
            return "{} {} zdał kolokwium".format(self.imie,self.nazwisko)
        else:
            return "{} {} nie zdał kolokwium, bedzie musiał je poprawić w następnym terminie".format(self.imie,self.nazwisko)
    def zajecia(self):
        rozoczecie =[random.randint(7,12),random.randrange(0,45,15)]
        print("Masz dzisiaj zajecia, musisz w odpowiednim momęcie wyjść by być na czas ale nie pamietasz na którą miałeś tam przyjść.")
        przyjscie = [int(input("Podaj godzine na ktorą wyjdziesz: ")),int(input("Podaj minuty: "))]
        if przyjscie[0]==rozoczecie[0] and przyjscie[1]==rozoczecie[1]:
            return "Przyszedłeś idealnie na czas :)"
        elif przyjscie[0]<=rozoczecie[0] and przyjscie[1]<=rozoczecie[1]:
            return "Jesteś przed czasem"
        elif przyjscie[0]>=rozoczecie[0]+1:
            return "Spózniłeś się o na tyle że zajęcia się już skończyły"
        else:
            return "Spóźniłeś się, wejdź szybko do sali" 

people = Student("qwe","asx","43022","as","sadaxs")
print(people.wyswietldane())
print(people.kolokfium("sasas"))
print(people.zajecia())

        