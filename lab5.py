import random
import math
import statistics 

def zad1():
    tab = []
    srednia = 0
    n = random.randint(1,10)
    while n>0:
        a = float(input("Podaj liczbę"))
        if a < 0:
            continue
        
        tab.append(a)
        n-=1
    for i in tab:
        srednia = srednia+i
    srednia = srednia/len(tab)
    print("Srednia wynosi ",srednia)
def zad2():
    n = int(input("Podaj liczbę"))
    x = int(input("Podaj liczbę"))
    tab = []
    j = 0
    '''if n== 0 or x== 0:
        break'''
    for i in range(n,x):
        if j == 5:
            break
        tab[j]=i
        j+=1
    print(min(tab))
    print(max(tab))
    print(statistics.median(tab)) 
def zad3():
    liczba = input("Podaj liczbe: ")
    i = 0 
    j = 0
    palidrom = True
    while i<len(liczba)/2:
        if liczba[i]!=liczba[len(liczba)-i-1]:
            palidrom = False
            break
        i+=1
    if palidrom == True:
        print("Liczba jest palidromem ",liczba)
    else:
        for i in range (len(liczba)-1,-1,-1):
            print(liczba[i],end="")
def zad4():
    n = int(input("Ile liczb?"))
    while True:
        if n==0:
            break
        liczba = int(input("Podaj liczbe: "))
        if -6<liczba<6:
            print("Liczba jest w przedziale")
        n-=1
def zad5():
    suma = 0 
    i = 0
    wieksze = False
    while i<101:
        suma = suma + i**3
        if suma > 10**6 and wieksze == False:
            print("Trzeba dodać ", i," liczb")
            wieksze = True
        i+=1
    print("Suma wynosi: ",suma)
def zad6():
    liczba = random.randint(1,100)
    for i in range (3,0,-1):
        zgadywana = int(input("Zgadnij liczbę: "))
        if zgadywana == liczba:
            print("Gratulacje udało ci się :D")
        elif zgadywana<liczba:
            print("Podałeś za małą liczbę, zostało ", i-1," prób")
        else:
            print("Podałeś za dużą liczbę, zostało ", i-1," prób")
    print("Była to liczba: ",liczba )
def zad7():
    print("   /\___/\ (( ")
    print("   \`@_@'/ ))")
    print("   {_:Y:.}_//")
    print("--{_}^-'{_}--")


zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4,
    "5": zad5,
    "6": zad6,
    "7": zad7
}
x = input("Podaj numer zadania: ")
zadania[x]()



        
    

