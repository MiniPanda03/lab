
import math

def zad1():
    i = 1
    while i<=100:
        print(i,"To jest efekt pętli while")
        i+=1
def zad2():
    i=254
    while i<321:
        if i%2!=0 and i%5==0:
            print(i)
        i+=1
    j = -320
    while j<-255:
        if j%2!=0 and j%5==0:
            print(j)
        j+=1
def zad3():
    while True:
        x = int(input("Podaj liczbę"))
        if x%12==0:
            print("podałeś liczbe podzielną przez 12 więc kończę pętle")
            break
def zad4():
    sum = 0
    dl = 0
    while True:
        try: 
            x = float(input("Podaj liczbę: "))
        except ValueError: 
            print("Poniewaz podano niepoprawny rodzaj danych konczy dzialanie")
            break
        if x == 0.0:
            print("Wpisano 0")
            break
        sum = sum + x
        dl+=1
        print("Średnia wynosi: ", sum/dl)
def zad5():
    suma= 0
    dl = 0
    while True:
        a = int(input("Podaj liczbę"))
        dl +=1
        suma = suma + a
        if sum/dl == 66:
            print("Średnia jest rowna 66")
            break
        elif sum >100:
            print("Suma jest wieksza od 100")
            break
def zad6(n):
    dzielniki = []
    sum = 0
    for i in range (1,int(round(n/2,0))+1):
        if n%i==0:
            dzielniki.append(i)
    for j in dzielniki:
        sum+=j
    if sum == n:
        print("Liczba jest doskonała")
    else:
        print("Liczba nie jest doskonała")
def zad7(n):
    dzielniki = []
    sum = 0
    for i in range (1,int(round(n/2,0))+1):
        if n%i==0:
            dzielniki.append(i)
    if len(dzielniki)==1:
        print("Liczba jest liczbą pierwsza")
    else:
        print("Liczba nie jest liczbą pierwszą")
def zad8(n):
    mies = 1
    oszczednosci = 0
    while mies <n:
        oszczednosci +=333
        oszczednosci= oszczednosci+oszczednosci*0.08
        n-=1
    print("Oszczedził: ",oszczednosci,"zł")
def zad9(sum):
    while True:
        i = int(input("Podaj liczbę"))
        roznica = math.fabs(sum-i)
        if roznica<5:
            print("Roznica mniejsza niz 5 i wynosi: ", roznica)
            break
        print(roznica)
        sum = i
def zad10(liczba):
    while True:
        liczba1 = int(input("Podaj liczbę: "))
        sum = liczba1 +liczba
        print("Suma wynosi: ", sum)
        if liczba == liczba1:
            print("Liczby sa takie same")
            break
        liczba = liczba1

zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4,
    "5": zad5,
    "6": zad6,
    "7": zad7,
    "8": zad8,
    "9": zad9,
    "10": zad10
}
x = input("Podaj numer zadania: ")
if int(x)>5:
    n = int(input("Podaj liczbę: "))
    zadania[x](n)
else:
    zadania[x]()

        
        



        




    