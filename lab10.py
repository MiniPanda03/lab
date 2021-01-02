def zad1():
    tekst = "          Magia jest w opinii niektórych ucieleśnieniem Chaosu. Jest kluczem zdolnym otworzyć zakazane drzwi. Drzwi, za którymi czai się koszmar, zgroza i niewyobrażalna okropność, za którymi czyhają wrogie, destrukcyjne siły, moce czystego zła, mogące unicestwić nie tylko tego, kto drzwi te uchyli, ale i cały świat. A ponieważ nie brakuje takich, którzy przy owych drzwiach manipulują, kiedyś ktoś popełni błąd, a wówczas zagłada świata będzie przesądzona i nieuchronna. Magia jest zatem zemstą i orężem Chaosu. To, że po Koniunkcji Sfer ludzie nauczyli posługiwać się magią, jest przekleństwem i zgubą świata. Zgubą ludzkości. I tak jest. Ci, którzy uważają magię za Chaos, nie mylą się.                   "
    tekst2 = reversed(tekst)
    print("Działanie lower: \n",tekst.lower())
    print("Działanie reversed: \n",tekst2)
    print("Działanie swapcase: \n",tekst.swapcase())
    print("Działanie capitalize: \n",tekst.capitalize())
    print("Działanie replace: \n",tekst.replace("Chaosu", "kotów"))
    print("Działanie lstrip: \n",tekst.lstrip())
    print("Działanie rstrip: \n",tekst.rstrip())
    print("Działanie count: \n ',' występuje:",tekst.count("a"))
    print("Działanie find: \n Czy jest słowo koszmar? ",tekst.find("koszmar"))
    print("Działanie isalnum: \n Czy jest alfanumeryczne? ",tekst.isalnum())
    print("Działanie startswith: \n Czy zaczyna sie od Meh? ",tekst.startswith("Meh"))
    print("Działanie endswith: \n Czy konczy sie . ? ",tekst.endswith("."))
def zad2():
    dane = [["imie",""],["nazwisko",""],["numer telefonu",""],["rozmiar buta",""],["Twoje imie jest "]]
    for i in range (4):
        dane[i][1] = input(f"Podaj {dane[i][0]}:")
        nazwa = dane[i][0]
        if i < 2:
            dane[i][1] = dane[i][1].lower().capitalize()
            dane[i][0] = "Twoje "+dane[i][0]
        else: 
            dane[i][1] = dane[i][1].replace("+","").replace("-","").replace(" ","")
            dane[i][0] = "Twój "+dane[i][0]
        print(f"Podane {nazwa} składa się tylko z liczby? ",dane[i][1].isdigit())
    for i in range (4):
        print(f"{dane[i][0]}: {dane[i][1]}",end=", ")
    if dane[0][1][len(dane[0][1])-1] != "a" or dane[0][1] == "Barnaba"or dane[0][1]=="Bonawentura" or dane[0][1]=="Kosma" or dane[0][1]=="Zawisza":
        print("Imie jest męskie")
    elif dane[0][1][len(dane[0][1])-1] == "a" or dane[0][1]=="Nel":
        print("Imie jest damskie")
def zad3():
    tekst = "Długo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'."
    tekst = tekst.split(".")
    print(tekst[0])
    tab = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."] # funkcja join()?
    zdanie = ""
    for i in tab:
        if i == "psem":
            zdanie+=i
        else:
            zdanie= zdanie+i+" "
    print(zdanie)

''' Zad 4 
Metody związane z zmianą  przydają się przy pracy z danymi - po to by sposób zapisania danych był taki sam i 
po to by sprawdzić czy użytkownik dobrze wpisał swoje dane. Tez gdy jest coś wysyłane do dużej ilości osób
możemy sobie wytwarzany tekst odpowiednio zrobić i zaprogramować by zmieniać niektóre części tekstu.
''' 
zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3
}
x = input("Podaj numer zadania: ")
zadania[x]()