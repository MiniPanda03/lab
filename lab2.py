import math

def zad1(a):
    b= int(input("Podaj liczbe"))
    if (a%b==0): 
        print("Tak") 
    elif (b==0): 
        print("Nie można dzielić przez 0")
    else: 
        print("Nie jest podzielne")
def zad2(a):
    if a<=10:
        print("Cos")
    elif 10<a<=25:
        print("Cos1")
    else:
        print("Cos3")
def zad3(a):
    b = int(input("Podaj liczbe"))
    c = int(input("Podaj liczbe"))
    if a> b:
        if a == c:
            print("1 i 2 są równe")
        elif a>c:
            print("1 jest najwieksza")
    elif b > c:
        print(b)
    elif b == c:
        print("2 i 3 sa rowne")

        print(c)
def zad4(a):
    if a>0:
        print("dodatnia")
    elif a<00:
        print("ujemna")
    if a%2 == 0:
        print("Podzielna przez 2")
    else:
        print("reszta z dzielenia",a%2)
def zad5():
    a = float(input("Podaj wydychane"))
    if 0.1>a>0.25:
        print("po spozyciu alko")
    elif a>0.25:
        print("stan nietrzezwosci")
    else:
        print("Mozesz jechac")
def zad6(a):
    b = float(input("Podaj liczbe"))
    c = float(input("Podaj liczbe"))
    d = float(input("Podaj liczbe"))
    if a>b and a>c and a>d:
        print("Najwieksza liczba jest liczba a ktora wynosi:",a)
    elif b>c and b>d:
        print("Najwieksza liczba jest liczba b ktora wynosi:",b)
    elif c>d:
        print("Najwieksza liczba jest liczba c ktora wynosi:",c)
    else:
        print("Najwieksza liczba jest liczba d ktora wynosi:",d)
def zad7():
    a = int(input("Podaj liczbe przy x2 "))
    b = int(input("Podaj liczbe przy x "))
    c = int(input("Podaj liczbe koncowa "))
    delta = b**2-4*a*c
    if delta > 0:
        x1= (-b-math.sqrt(delta))/2*a
        x2= (-b+math.sqrt(delta))/2*a
        print("Rozwiązania to "+ str(x1) +" i "+ str(x2) )
    elif delta ==0:
        x = -b/2*a
        print("Rozwiązanie to",x)
    else:
        print("Brak rozwiązań")
def zad8():
    a = int(input("Podaj długość boku: "))
    b = int(input("Podaj długość boku: "))
    c = int(input("Podaj długość boku: "))
    if a<=0 or b<=0 or c<=0:
        print("Boki nie mogą mieć długość ujemną lub rowną 0")
    else:
        if a>b and a>c:
            a,c=c,a
        elif b>c:
            b,c = c,b 

        if c**2 == a**2+b**2:
            print("trojkat jest prostokatny")
        else:
            print("Trojkąt nie jest prostokątny")
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
if int(x) == 6 or (int(x)>0 and int(x)<5):
    a = float(input("Podaj liczbe"))
    zadania[x](a)
else:
    zadania[x]()
# W tych zadaniach ktorych sie powtarzalo "Podaj liczbe" dalam to do argumentu funkcji 