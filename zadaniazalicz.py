import random
import datetime

def netto(placa):
    chorobowa = 0.0976 *placa
    rent = 0.015 *placa
    emerytalne = 0.0245 * placa
    wartosc = placa - rent - emerytalne - chorobowa 
    wartosc = wartosc - 0.09*wartosc #zdrowotne
    if wartosc*12 < 85528:
        wartosc = wartosc - wartosc*0.17
    else:
        wartosc = wartosc - wartosc*0.32
    return round(wartosc,2)
def brutto(placa):
    if placa*12 < 85528:
        wartosc = placa/0.83
    else:
        wartosc = placa/0.68
    wartosc = wartosc/0.91 #ze zdrowotnego
    wartosc = wartosc/0.8629 #choroba,emerytalne,rent
    return round(wartosc,2)
def zad1(placa,rodzaj):
    if rodzaj == "netto":
        return brutto(placa)
    elif rodzaj == "brutto":
        return netto(placa)
def zad2(placa,rodzaj):
    if rodzaj == "brutto":
        placa = netto(placa)
    wydatki = placa*0.0976 #emerytalne
    wydatki = wydatki + placa*0.065 #rentowe
    wydatki = wydatki + placa*0.0167 #wypadkowe
    wydatki = wydatki + placa*0.0245 #FP
    wydatki = wydatki + placa*0.001 #FGŚP
    return "Wydatki wynoszą: "+str(round(wydatki,2))+" zł"
def zad3(nazwa):
    wynik = 0
    maks = 0
    plik = open("sprawdzian.txt", "w",encoding="utf-8")
    plik.write("Imie i nazwisko: "+nazwa+" \n")
    sprawdzian = [["Przeglądarką internetową nie jest (wskaż tylko jedną odpowiedź): \n a) Internet Explorer,\n b) Mozilla Firefox,\n c) Google,\n d) Opera.","c",1],["Podaj nazwe modułu który importujesz przy potrzebie losowania liczb: ","random",2],["Które polecenie systemu Windows należy wykonać, aby sprawdzić, ile ruterów pośrednich jest pomiędzy hostem źródłowym a docelowym? \n a)routeprint, \n b)ipconfig \n c)tracert \n d)apr","c",1],["1 kilobajt - ile to bajtów?","1024",2],["Liczba 1011 w systemie binarnym będzie wynosić w dziesiątkowym: ","11",2],["Rozwiń skrót RAM: ","random access memory",2],["Jaka liczba nie ma wartości True? ","0",2],["Tworząc tabelę w języku SQL, zdefiniowano dla kolumny klucz główny. Aby zabezpieczyć ją przed wstawieniem wartości pustej, należy zastosować atrybut\n a) NULLB, \n b)UNIQUE, \n c)DEFAULT, \n d)NOT NULL","d",1],["Co NIE wpływa na utratę danych z pamięci masowej HDD? \n a)Zniszczenie talerzy dysku \n b)Sformatowanie partycji dysku \n c)Fizyczne uszkodzenie dysku \n d)Utworzena macierz dyskowa RAID 5","d",1],["Co trzeba wpisać w cmd by sprawdzić IP karty sieciowej?  ","ipconfig",2]]
    for i in range(10):
        wybrane = random.randint(0,len(sprawdzian)-1)
        print(i+1,sprawdzian[wybrane][0])
        odpowiedz=input("Odpowiedz: ")
        plik.write(str(sprawdzian[wybrane][0])+"\n Podana odpowiedź: "+odpowiedz)
        maks = maks+sprawdzian[wybrane][2]
        if odpowiedz.lower().lstrip().rstrip() == sprawdzian[wybrane][1]:
            wynik = wynik+sprawdzian[wybrane][2]
            plik.write("\n Uzyskane punkty: "+str(sprawdzian[wybrane][2])+" \n")
        else:
            plik.write("\n Uzyskane punkty:0 \n")
        sprawdzian.pop(wybrane)
    if wynik < 0.5*maks:
        ocena = "2"
    elif 0.5*maks< wynik<0.71*maks:
        ocena = "3"
    elif 0.71*maks< wynik<0.9*maks:
        ocena = "4"
    elif maks*0.9<wynik:
        ocena = "5"
    plik.write("Uzyskane całkowity wynik: "+str(wynik)+"/"+str(maks)+"\nUzyskana ocena: "+ocena)
    plik.close()
    return "Otrzymałeś wynik: "+str(wynik)+" z "+str(maks)+" przez to uzyskałeś ocene "+ocena
def zad4(liczba,przedrostek):
    znacznik ={
        "kB": 10**3,
        "MB": 10**6,
        "GB": 10**9,
        "TB": 10**12
    }
    wynik = liczba*znacznik[przedrostek]/1024/1024/1024
    return "Prawdziwa wartość wynosi: "+str(wynik)+" GB"
def zad5(ilosc,znacznik):
    rodzaj = {
        "THB": 0.033,
        "BTC": 32249.90,
        "BTN": 0.014,
        "MRO": 0.028,
        "ETH": 1317.43 
    }
    if znacznik.upper().lstrip().rstrip() =="USD":
        print("Wartość w THB: "+str(ilosc/rodzaj["THB"]))
        print("Wartość w BTC: "+str(ilosc/rodzaj["BTC"]))
        print("Wartość w BTN: "+str(ilosc/rodzaj["BTN"]))
        print("Wartość w MRO: "+str(ilosc/rodzaj["MRO"]))
        return "Wartość w ETH: "+str(ilosc/rodzaj["ETH"])
    else: 
        return "Wartość w USD: "+str(ilosc*rodzaj[znacznik])
def zad6(temp,rodzaj):
    if rodzaj.rstrip().lstrip().upper() != "F":
        faren = zmianatemp(temp,rodzaj)
    else:
        zmianatemp(temp,rodzaj)
    else:
        faren = temp
        zmianatemp(temp,rodzaj)
    if faren <= 32.0:
        return "Brrr woda zamarzła "+str(temp)+" "+rodzaj
    elif faren >= 212.0:
        return "Woda wrze "+str(temp)+" "+rodzaj
    else:
        return "Woda ma temperature: "+str(temp)+" "+rodzaj
def zmianatemp(temp,rodzaj):
    if rodzaj.rstrip().lstrip().upper() == "K":
        faren = (temp*1.8)-459.67
        print("W Celsjuszach: "+str(temp-273.15)) #	°C = K − 273.15
        print("W Farenheit: "+str(faren)) #°F = (K × 1.8) - 459.67
        print("W Rankine: "+str(temp*1.8)) #R = K x 1.8
        return faren
    elif rodzaj.rstrip().lstrip().upper() =="F": # Fahrenheit
        print("W Celsjuszach: "+str((temp-32)/1.8)) #°C = (°F − 32) /1.8
        print("W Kelvinach: "+str((temp+459.67)*5/9)) #	K = (°F + 459.67) × 5/9
        print("W Rankine: "+str(temp+459.67)) #	°R = °F + 459.67
    elif rodzaj.rstrip().lstrip().upper() == "R": #Rankine 
        faren = temp-459.67
        print("W Celsjuszach: "+str((temp/1.8)-273.15)) #°C = (°R ÷ 1.8) – 273.15
        print("W Farenheit: "+str(faren)) #°F = °R - 459.67
        print("W Kelvinach: "+str(temp/1.8)) #K = R/1.8
        return faren
    elif rodzaj.rstrip().lstrip().upper()== "C":
        faren = (temp*1.8)+32
        print("W Kelvinach: "+str(temp+273.15)) #	K = °C + 273.15
        print("W Farenheit: "+str(faren)) #°F = (°C × 1.8) + 32
        print("W Rankine: "+str((temp+273.15)*1.8)) #°R = (°C + 273.15) × 1.8
        return faren
    else:
        print("Nieznany rodzaj")
def wielkanoc(rok):
    if rok=="":
        data = datetime.datetime.now()
        rok = int(data.strftime("%Y"))
    a = rok%19
    b =rok%4
    c=rok%7
    d = (19*a+24)%30
    e= (2*b+4*c+6*d+5)%7
    niedz = 22+d+e
    if niedz>31:
        niedz = d + e - 9
        return "Wielkanoc wypada: "+str(niedz)+" kwietnia"
    else:
        return "Wielkanoc wypada: "+str(niedz)+" marzec"
def zad7(data):
    if data=="":
        data = datetime.datetime.now()
    else:
        data =data.rsplit("-")
        data = datetime.datetime(data[2],data[1],data[0])
    jutro = data + datetime.timedelta(days=1)
    wczoraj = data + datetime.timedelta(days=-1)
    uro = input("Podaj datę swojich urodzin (Zapisz D-M-R): ")
    uro =uro.rsplit("-").rstrip().lstrip()
    uro = datetime.datetime(int(uro[2]),int(uro[1]),int(uro[0]))
    print("Twoje urodziny wypadły w: "+str(uro.strftime("%A")))
    print(wielkanoc(input("Podaj rok z którego chcesz dowiedzieć się kiedy była/będzie Wielkanoc \n (Jeśli nie wpiszesz to bedzie wyświetlona data wielkanocy w tym roku):")))
    return "Jutro będzie: "+str(jutro.strftime("%x"))+", a wczoraj było: "+str(wczoraj.strftime("%x"))

zadania = {
    "1": zad1,
    "2": zad2,
    "3": zad3,
    "4": zad4,
    "5": zad5,
    "6": zad6,
    "7": zad7
}
tekst = [["Podaj ilosć pieniędzy: ","Jest to brutto czy netto? "],["Podaj płace swojego pracownika: ","Jest to brutto czy netto?"],"Podaj swoje imie i nazwisko: ",["Podaj pojemność (liczbowo) dysku zapisaną na pudełku","Podaj jednostkę: "],["Podaj ilość pieniędzy: ","Podaj znacznik waluty: (tj USD,BTC itp.) "],["Podaj temperature: ","Podaj jednostke: (K,C,F,R) "],"Podaj datę: (jeżeli nie będzie podana to zostanie dana data dzisiejsza) "]
while True:
    wybor = input("Podaj numer zadania: ")
    if 0<int(wybor)<3 or 3<int(wybor)<7:
        print(zadania[wybor](int(input(tekst[int(wybor)-1][0])),input(tekst[int(wybor)-1][1])))
    else:
        print(zadania[wybor](input(tekst[int(wybor)-1])))
    if input("Czy chcesz zakończyć? ").rstrip().lstrip().lower() =="tak":
        break
    