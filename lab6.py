import random
def zad1():
    i = 0
    tab = ["q","w","e","r","t","y","u","i","o","p"]
    while i<=8:
        print(tab[i])
        if i == 6:
            i+=2
        else:
            i+=3
def zad2():  
    tab = []
    for i in range(10):
        tab.append(random.randint(1,100))
    i = 0
    while i<=8:
        print(tab[i])
        if i == 6:
            i+=2
        else:
            i+=3
def zad3():
    tab = []
    licz= 0
    for i in range(10):
        tab.append(random.randint(1,59))
    tab.append(14)
    tab.insert(len(tab),16)
    tab.append(44)
    print(tab)
    licz = 0
    n = 10
    for i in range (n):
        if tab[i]%2!=0:
            tab.pop(i)
            n-=1
            licz+=1
        if licz == 2:
            break
    for i in range (n):
        if tab[i]%2!=0:
            tab.remove(tab[i])
            break
    print(tab)
    tab.pop(4)
    tab.insert(4,3)
    tab.pop(9)
    tab.insert(9,33)
    print(tab)
def zad4():
    n = int(input("Podaj liczbe"))
    dzielniki = []
    for i in range (1,int(round(n/2,0))+1):
        if n%i==0:
            dzielniki.append(i)
    print("Dzielniki to:",dzielniki)
def zad5():
    tab = []
    tab2 = []
    powt = []
    n = int(input("Podaj dlugosc tablicy"))
    x =int(input("Podaj poczatek zakresu"))
    z = int(input("Podaj koniec zakresu"))
    for i in range(n):
        tab.append(random.randint(x,z))
    print(tab[-3])
    print(tab)
    while True:
        k = int(input("Podaj ktory element chcesz usunac od konca"))
        if k < len(tab)-1:
            break
        print("Liczba jest poza zakresem, prosze podac liczbe w zakresie do ",len(tab))
    tab.pop(-(k))
    print(tab)
    for i in range(n):
        tab2.append(random.randint(x,z))
    tab = tab + tab2
    print(tab)
    for i in range(len(tab)):
        if powt.count(tab[i])==0:
            print(tab[i]," : ",tab.count(tab[i]))
            powt.append(tab[i])
def zad6():
    tab = []
    n = int(input("Podaj dlugosc tablicy"))
    x =int(input("Podaj poczatek zakresu"))
    z = int(input("Podaj koniec zakresu"))
    for i in range(n):
        tab.append(random.randint(x,z))
    tab2 = list(dict.fromkeys(tab))
    print("Po usunięciu ", tab)
def zad7():
    lotto = []
    losowanie = []
    traf = 0
    while True:
        wybor = int(input("Wybierz forme wybrania liczb (Wpisanie: 1, chybił trafił: 2) "))
        if wybor==1 or wybor==2:
            break
    while True:
        n = random.randint(1,49)
        if lotto.count(n)==0:
            lotto.append(n)
        if len(lotto)==6:
            break
    if wybor == 1:
        while True:
            try:
                n = int(input("Wybierz liczbę od 1 do 49: "))
            except ValueError:
                print("Podaj liczby a nie zostawiaj pustą kratkę ;)")
            if losowanie.count(n)>0:
                print("Nie podawaj tych samych liczb")
            elif n>49 or n<1:
                print("Podawaj liczby tylko z przedziału 1 do 49")
            else:
                losowanie.append(n)
            if len(losowanie)==6:
                break
    elif wybor == 2:
        while True:
            n = random.randint(1,49)
            if losowanie.count(n)==0:
                losowanie.append(n)
            if len(losowanie)==6:
                break
    for i in lotto:
        for j in losowanie:
            if i == j:
                traf+=1
    print(losowanie)
    if traf<3:
        print("nic nie wygrales")
    elif traf == 3:
        print("wygrales 100zl")
    elif traf == 4:
        print("wygrales 10 000zl")
    elif traf ==5:
        print("wygrales 500 000zl")
    elif traf ==6:
        print("wygrales 10 000 000zl")
def zad8():
    tab = []
    wybrane = []
    n = int(input("Ile liczb? "))
    while n > 0:
        tab.append(random.randint(1,100))
        n-=1
    print("Lista:",tab)
    if len(tab)%2==0:
        n=0
    else:
        n=1
    while n<len(tab):
        liczba = random.randint(0,len(tab)-1)
        liczba2 = random.randint(0,len(tab)-1)
        if wybrane.count(liczba)==0 and wybrane.count(liczba2)==0:
            wybrane.append(liczba)
            wybrane.append(liczba2)
            tab[liczba],tab[liczba2]=tab[liczba2],tab[liczba]
            n+=2
    print("Lista po rozmieszaniu:",tab)
    sortowanie = int(input("Jakie sortowanie? 1 -od najwiekszej 2 -od najmniejszej"))
    if sortowanie == 1:
        tab.sort(reverse=True)
        print("Po posortowaniu: ",tab)
    else:
        tab.sort()
        print("Po posortowaniu: ",tab)
def zad9():
    tab= []
    n = int(input("Ile liczb? "))
    while n>0:
        tab.append(int(input("Wybierz liczbę")))
        n-=1
    tab.sort()
    print("Największa liczba: ",tab[len(tab)-1])
    while n < len(tab):
        print(tab[n]," powtarza się: ",tab.count(tab[n]))
        n+=tab.count(tab[n])
def zad10():
    a= 0 
    b=1
    n = int(input("Podaj ile liczb ma byc wyliczone"))
    while n>0:
        if a==0:
            print(a)
            a = a+b
        elif a>b:
            b = a+b
            print(b)
        else:
            a= a+b
            print(a)
        n-=1
def zad11():
    n = int(input("Podaj liczbe"))
    if n < 2:
        print("NIe ma liczb pierwszych w tym zakresie")
    else:
        skr = [False] * (n + 1)
        i = 2
        while i * i <= n:
            if  not skr[i]:
                j = i * i            
                while j <= n:
                    skr[j] = True
                    j += i
            i += 1
        for i in range(2, n+1):
            if not skr[i]:
                print(i)
    

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
    "11": zad11
}
x = input("Podaj numer zad")
zadania[x]()