import datetime

def zad1():
    zmienna1 = int(input("Podaj 1 liczbę:"))
    zmienna2 = int(input("Podaj 2 liczbę:"))
    suma = zmienna1 + zmienna2
    iloczyn = zmienna1 * zmienna2
    iloraz = zmienna1 / zmienna2
    roznica= zmienna1 - zmienna2
    print("Suma:",suma,", roznica:",roznica,", iloczyn: ",iloczyn,"iloraz:",iloraz)
def zad2():
    dane = [1,69,666,1000,1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000]
    print(dane[4]%dane[0])
def zad3():
    swiatlo = 299792 
    rok= 31557600
    predkosc = swiatlo* rok
    print(predkosc)
def zad4():
    min = 60
    godz = 60 * min
    doba = godz * 24
    rok = doba * 365.25
    x = datetime.datetime.now()
    dzien=int(input("Podaj dzien urodzenia:"))
    miesiac = int(input("Podaj miesiac urodzenia w liczbie:"))
    rokuro = int(input("podaj rok urodzenia:"))
    y = datetime.datetime(rokuro, miesiac, dzien)
    roznica = x - y 
    print(type(roznica))
def zad5():
    dlugosc = int(input("Podaj długość:"))*2.5
    print("W centymetrach to:",dlugosc)
def zad6():
    droga = 30
    czas = 0.25 
    czas2 = 12/60
    print("Średnia prędkość w km/h",droga/czas)
    print("Średnia w 2 przypadku",droga/czas2)

zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4,
    "5": zad5,
    "6": zad6
}
x = input("Podaj numer zadania: ")
zadania[x]()