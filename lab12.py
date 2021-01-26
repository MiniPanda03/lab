import math

def zad1(a,b,c):
    if c == 1:
        return "Suma wynosi: ", a+b
    elif c ==2:
        return "Różnica wynosi: ",a-b
    elif c == 3:
        return "Iloczyn wynosi: ",a*b
    elif c == 4:
        return "dzielenie wynosi: ",a/b
    elif c==5:
        return "Pierwiastkowanie liczby ",a," wynosi: ", math.sqrt(a),",a dla ",b," wynosi: ",math.sqrt(b)
def stozek (r,h,l):
    pole = 3.14*r*(r+l)
    objetosc = 3.14*r**2*h/3
    return "Pole stożka wynosi: "+str(pole)+" a objętość: "+str(objetosc)
def kula (r):
    return "Pole kuli wynosi: "+str(4*3.14*r**2)+" a objętość: "+str(4/3*3.14*r**3)
def szescian (a):
    return "Pole sześcianu wynosi: "+str(6*a**2)+" a objętość: "+str(a**3)
def zad2(wybor):
    r = float(input("Podaj długość boku/promień:"))
    if wybor == 1:
        return stozek(r,float(input("Podaj wysokość: ")),float(input("Podaj l: ")))
    elif wybor ==2:
        return kula(r)
    elif wybor==3:
        return szescian(r)
def zad3(liczba):
    cm = liczba * 30.48
    m = cm * 0.01
    mm = cm * 10
    km = m * 0.001
    return "Długość wynosi: "+str(mm)+" mm, "+str(cm)+" cm, "+str(m)+" m i"+str(km)+" km"
def zad4(wysokosc):
    if wysokosc<5000:
        return "za nisko"
    else:
        return "bezpiecznie"
    return w/1000
def bmi(wzrost,masa):
    masa = int(masa)
    if wzrost<0 or masa<0:
        return "Podałeś niepoprawną mase lub wzrost"
    else:
        wskaznik = masa/wzrost**2
        if wskaznik<18.5:
            return "Masz niedowagę"
        elif 18.5 < wskaznik < 24.99:
            return "Twoja waga jest prawidłowa"
        else:
            return "Masz nadwagę!!!"
def zad6(wybor,n):
    n = int(n,wybor)
    print("Liczba binarnie: ", bin(int(n)))
    print("Liczba ósemkowo: ",oct(int(n)))
    print("Liczba szesnatkowo", hex(int(n)))
    print("Liczba dziesiętnie:", n)
    return "Podaną liczba wynosi: ",n
def zad7(liczba):
    rzymskie = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
    wynik = []
    for i in range(len(rzymskie)):
        licz = int(liczba / rzymskie[i][0])
        wynik.append(rzymskie[i][1] * licz)
        liczba -= rzymskie[i][0] * licz
    return ''.join(wynik)
zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4,
    "5": bmi,
    "6": zad6,
    "7": zad7
}
tekst = [["Podaj liczbe","Wybierz:(1-suma;2-roznica;3-iloczyn;4-dzielenie;5-pierwiastkowanie): "],"Co chcesz obliczyć?: (1-stozek;2-kula;3-szescian)","Podaj wartość w stopach: ","Na jakiej wysokości lecimy? [w metrach]: ",["Podaj wzrost: ","Podaj mase: "],["Wybierz rodzaj liczby: ","Wpisz liczbę: "],"Podaj liczbe: "]
wybor = input("Podaj numer zadania: ")
x = int(wybor)
if x == 1:
    print(zadania[wybor](int(input(tekst[x-1][0])),int(input(tekst[x-1][0])),int(input(tekst[x-1][1]))))
elif 4<x<7:
    print(zadania[wybor](int(input(tekst[x-1][0])),input(tekst[x-1][1])))
else:
    print(zadania[wybor](int(input(tekst[x-1]))))