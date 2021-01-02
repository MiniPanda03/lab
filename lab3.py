import random
def zad1():
    for i in range (1,100):
        if i%8==0:
            print(i)
def zad2(n):
    for i in range(n,0,-1):
        if i%9==0 or i%6==0:
            print(i)
def zad3():
    for i in range (100,200):
        if i%2!=0 and i%3!=0:
            print(i)
def zad4():
    for i in range (100,200,2):
        if i%5!=0 and i%6!=0 and i%11!=0:
            print(i)
def zad5(x):
    silnia=1
    for i in range (1,x,1):
        silnia=silnia*i
def zad6(x):
    gwiazdki = "*"
    for i in range (x):
        liczba= x-i
        print(" "*liczba+gwiazdki+" "*liczba)
        gwiazdki = "*" + gwiazdki + "*"
def zad7(n):
    for i in range(1,n+1):
        print(2**i)
def zad8():
    wieksza = 0 
    for i in range (10000):
        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0: 
            if wieksza<i:
                wieksza = i
    print(wieksza)
def zad9():
    print("Liczby w lotto to:")
    for i in range (6):
        print(random.randint(1,49))
def zad10():
    print("Liczby w multi multi to:")
    for i in range(10):
        print(random.randint(1,80))
def zad11():
    print("Liczby w mini lotto to:")
    for i in range (5):
        print(random.randint(1,42))
def zad12():
    reszka = 0 
    orzel = 0
    for i in range (50):
        if random.randint(0,1)==1:
            orzel+=1
        else:
            reszka+=1
    print("Wylosowano orzeł:",orzel," a reszka",reszka)

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
    "10": zad10,
    "11": zad11,
    "12": zad12
}
x = input("Podaj numer zadania: ")
if int(x) == 2 or (int(x)>4 and int(x)<8):
    n = int(input("Podaj liczbę: "))
    zadania[x](n)
else:
    zadania[x]()