import math
import random

def zad1():
    wysokosc = 2.5 
    sciana1 = 3 
    sciana2 = 5
    drzwi = 0.8 * 2
    okna = 0.6 * 0.6
    print("Pokoj bez drzwi i okien",sciana1*wysokosc*2+sciana2*wysokosc*2, "m2")
    print("Pokoj z drzwiami i oknem",wysokosc*sciana1*2+wysokosc*sciana2*2-okna-drzwi, "m2")
def zad2():
    temp = float(input("Podaj temperature: "))
    temp = (temp*1.8)+32 
    if temp < 32.0:
        print("Brrr woda zamarzła ", temp)
    elif temp > 212.0:
        print("Woda wrze ", temp)
    else:
        print("Woda ma temperature: ", temp)
def zad3():
    kat = int(input("Podaj rozmiar kąta: "))
    print ("Sinus: ",math.sin(kat))
    print ("Cosinus: ",math.cos(kat))
    print ("Tangens: ",math.tan(kat))
    print("Cotangens: ", 1/math.tan(kat))
def zad4():
    wybor = 0
    while True:
        if wybor == 0 or wybor>2:
            try : 
                wybor = int(input("Z jakiego rodzaju jednostki bedziesz chciał przeliczyć? (1-stopy,2-cale)"))
            except ValueError:
                continue
        try: 
            num = float(input("Podaj liczbę"))
        except ValueError:
            continue
        if wybor == 1:
            num = num* 30.48
        else:
            num = num*2.54
        print("Wpisana liczba w cm to: ",num)
        print("W metrach: ",num/100.0)
        print("W km: ",num/100000.0)
def zad5():
    minimum = 5
    while True:
        try:
            wysokosc = int(input("Podaj wysokosc lotu w metrach: "))
        except ValueError:
            continue
        if wysokosc/1000 < minimum:
            print(wysokosc/1000, "km to za nisko!")
        else:
            print("Na tej wysokości jesteś już bezpieczny")
            break
def zad6():
    wybor = int(input("Jakiego rodzaju bedzie liczba? (1-dec,2-bin,3-hex)"))
    n = input("Podaj liczbę: ")
    if wybor == 1:
        print("Liczba binarnie: ", bin(int(n)))
        print("Liczba ósemkowo: ",oct(int(n)))
        print("Liczba szesnatkowo", hex(int(n)))
    elif wybor == 2:
        n = "0b"+n
        n = int(n,2)
        print("Liczba ósemkowo: ",oct(int(n)))
        print("Liczba szesnatkowo", hex(int(n)))
    elif wybor == 3:
        n = "0x"+n
        n = int(n,16)
        print("Liczba ósemkowo: ",oct(int(n)))
def zad7():
    print(-7**0.5)
def zad8():
    liczba = random.randint(1,1000)
    suma = 0
    for i in range(liczba):
        suma = suma + i**2
    print("Liczba wylosowana: ",liczba,", wynik dodawania:",suma)
zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4,
    "5": zad5,
    "6": zad6,
    "7": zad7,
    "8": zad8
}
x = input("Podaj numer zadania: ")
zadania[x]()