import random

def zad1():
    druzyny = ["Huragan Wołomin", "Jeziorak Iława","Karpaty Krosno","LZS Bobrówko","Liverpool","FC Barcelona","Lech Poznań","Arka Gdynia","Piast Gliwice","LZS Narewka","Olimpia Warszawa","Polonia Iłża","Polonia Jastrowie","SKP Słubice", "SKP Słupca","Tur Turek","UKS SMS Łódź","Tęcza Wielowieś","Żurawianka Żurawica","Jedność Boronów"]
    poddru = set()
    for j in range (10):
        poddru.add(druzyny[random.randint(0,19)])
    return poddru
def zad2(druzyny,druzyny1,druzyny2,druzyny4):
    print("Działanie intersection: ",druzyny.intersection(druzyny4))
    print("Działanie difference: ",druzyny2.difference(druzyny1))
    print("Działanie union: ", druzyny.union(druzyny4))
    print("Działanie issuperset: Czy set druzyny zawiera set druzyny1? ", druzyny.issuperset(druzyny1))
    print("Działanie issubset: Czy set druzyny2 zawiera się w setcie druzyny4? ", druzyny2.issubset(druzyny4))
def zad3(druzyny,druzyny1,druzyny2,druzyny4):
    usun = list(druzyny2.difference(druzyny1))
    druzyny2.remove(usun[0])
    druzyny.pop()
    print("Po usunieciach sety druzyny2 i druzyny mają dlugość: ",len(druzyny2),len(druzyny))
    for i  in druzyny1:
        for j in druzyny4:
            if i == j:
                print("Set druzyny1 ma te samą dane w tym samym miejscu co druzyny4")
    druzyny4 = list(druzyny4) 
zad2(zad1(),zad1(),zad1(),zad1())
zad3(zad1(),zad1(),zad1(),zad1())
