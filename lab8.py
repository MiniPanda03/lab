import webbrowser

def zad1():
    menu = {}
    for i in range (5):
        x = input("wpisz pizze: ")
        menu[x] = int(input("wpisz cene: "))
    najdrosza = max(menu, key=menu.get)
    najtansza = min(menu, key=menu.get)
    print(menu)
    print(najdrosza,najtansza)
    del menu[najdrosza]
    del menu[najtansza]
    print(menu)
def zad2():
    tele = {}
    for i in range (3):
        x = input("wpisz imie: ")
        tele[x] = input("numer: ")
    print(tele)
    tele[next(iter(tele))] = int(input("Zmien telefon"))
    lista = tele.keys()
    print(lista)
    print(tele)
    tele[tele.keys(-1)] = int(input("Zmien telefon"))
    print(tele)
def zad3():
    uzytkownicy = {
        "admin": "admin",
        "admin2": "admin2",
        "admin3": "admin3",
        "admin4": "admin4",
        "admin5": "admin5",
        "admin6": "admin6"
    }
    x = input("Witmay na logowanku do brzydkich stron :) Podaj login: ")
    if x in uzytkownicy.keys():
        y = input("Podaj hasło: ")
        if uzytkownicy[x] == y:
            if x == "admin":
                webbrowser.open_new_tab("http://www.nyan.cat/")
            elif x == "admin2": 
                webbrowser.open_new_tab("https://www.hakaimagazine.com/wp-content/uploads/facebook-proboscis-monkeys.jpg")
            elif x == "admin3": 
                webbrowser.open_new_tab("https://docs.python.org/3/library/webbrowser.html")
        else: 
            print("Podałeś niepoprawne hasło ;( ")
    else:
        print("Nie mamy takiego uzytkownika")
def zad4():
    
    print("WYGRAJ PS5!!!! JEDYNE CO MUSISZ ZROBIC TO PODAC SWOJ MAIL BY WZIASC UDZIAL W WILEKIM LOSOWANIU!!!! (wcale nie scam po to by wysylac ci spam ;))")
    x = input("Podaj swoj nick/jak mamy sie do cb zwracac: ")
    serniczkowyspam[x] = input("Podaj mail: ")
    # mozna zrobic server do spamowania jak tak bardzo chce sie spamowac zdjeciami

zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4
}
x = input("Podaj numer zad")
zadania[x]()

