import sys
import random

def zad1():
    tupla = ("aaaa",1,"adsxz",56,23,"asdasd") 
    print("Długość tupli wynosi: ",len(tupla))
    print("Wielkość tupli: ",sys.getsizeof(tupla)," bajtów")
    tupla = tupla + ("aaaaasw",3231)
    print("Po dodaniu 2 elementow wielkosc wynosi: ",sys.getsizeof(tupla)," bajtów")
    tupla = list(tupla)
    print("Po zmanie na liste zajmuje: ", sys.getsizeof(tupla)," bajtów")
def zad2():
    tupla = []
    np = []
    for i in range (100):
        tupla.append(random.randint(0,10))
    tupla = tuple(tupla)
    for i in range(3):
        print(i," występuje: ",tupla.count(i)," razy")
    print("Liczby parzyste:")
    for i in range(100):
        if tupla[i]%2==0:
            print(tupla[i],end=", ")
        else:
            np.append(tupla[i])
    print('\n Liczby nieparzyste: ',np)
    # zamiana na listę pozwala na zmiane w tupli i potem znów listę zamienić na tuple
def zad3():
    A = []
    B = []
    for i in range(100):
        A.append(random.randrange(0,101,2))
        B.append(random.randrange(0,100,2)+1)
    A = tuple(A)
    B = tuple(B)
    print("Wielkość A: ",sys.getsizeof(A),"B , wielkość B: ",sys.getsizeof(B)," B")
    C = A+B
    print("Wielkość po połączeniu:", sys.getsizeof(A)," B")
    print("Długość połączonej tupli wynosi: ",len(C))
    for i in range (0,101,100):
        if C.count(i)>0:
            print("Tupla zawiera ",i)
            print("Miejsce przed połączeniem tupli ", id(A[A.index(i)]))
            print("Po połączeniu: ",id(C[C.index(i)]))
        else: 
            print("Tupla nie zawiera ",i)
def zad4():
    yes = ("qwe","meh","asd","aaa","poi","lkj")
    if "meh" in yes:
        print(True, " ,index: ",yes.index("meh"))
    nast = ("dame da ne dame yo ","dame na no yo anta ga suki de suki sugite","dore dake tsuyoi osake de mo yugamanai omoide ga baka mitai")
    i = input("Wprowadzi słowo:")
    powt = 0
    for j in range (len(nast)):
        if i in nast[j]:
            powt+=nast[j].count(i)
    print("Słowo występuje:", powt, " razy")
def zad5():
    krot = ("bark","krab")
    ang = True
    if len(krot[0])==len(krot[1]):
        for i in range (len(krot[0])):
            if not krot[0][i] in krot[1]:
                ang = False
                break
    else:
        ang = False
    if ang == False:
        print("Nie jest anagramem")
    else:
        print("Jest anagramem")

zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4,
    "5": zad5
}
x = input("Podaj numer zadania: ")
zadania[x]()