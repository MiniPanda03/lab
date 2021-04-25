
car_list = ["DWR226VJ","DWL231QW","WWA1209","POA06ED"]
parking = [["",""],["",""],["",""],["",""],["",""],["",""],["",""]]
class Car:
    def __init__(self,registration):
        self.registration = registration
        self.buy = False
        self.place = ""
    def buy_place(self,parking):
        free = []
        if self.buy == False:
            print("Witamy w naszym systemie do wynamowania miejsc parkingowych!")
            for i in range (len(parking)-1):
                if parking[i][1]=="":
                    free.append(i)
            if len(free)==0:
                return "Przepraszamy ale nie ma teraz dostępnych miejsc"
            print("Dostępne miejsca:")
            for i in free:
                print(str(i))
            place_choose = int(input("Wprowadż numer miejsca które chcesz zająć"))
            while True:
                if place_choose not in free:
                    print("Niestety miejsce które wprowadziłeś jest zajęte lub nie istnieje")
                    place_choose = int(input("Wprowadż numer miejsca które chcesz zająć"))
                else:
                    parking[place_choose][1]="Rev"
                    self.buy=True
                    self.place = place_choose
                    if parking[place_choose][0]!="":
                        for i in parking:
                            if i[0]=="":
                                i[0]=parking[place_choose][0]
                                print("Auto z rejestracją {} zostało przniesione do {} miejsca".format(i[0],parking.index(i)))
                                break
                        print("Niestety nie ma już niezapełnionych i niezarezerwowanych miejsc auto z rejestracją {} musi wyjechać".format(parking[place_choose][0]))
                    parking[place_choose][0] = ""
                    return "Udało ci się zarezerwować miejsce"
        return "Twoje auto jest juz zarejestrowane na naszym parkingu"
    def find_place(self,parking,car_list):
        if self.registration not in car_list:
            return "Twoje auto nie jest zapisane w naszym systemie proszę o skontaktowanie się z administratorem"
        print("Witamy na naszym parkingu")
        if self.buy == True:
            print("Widać że masz zarezerwowane miejsce :)")
            parking[self.place][0]=self.registration
            return "Twoje auto zaparkowało na miejscu {}".format(self.place)
        else:
            for i in parking:
                if i[0]=="":
                    i[0]=self.registration
                    self.place = parking.index(i)
                    return "Twoje auto zaparkowało na miejscu {}".format(parking.index(i))
                return  "Niestety nie mamy teraz dostępnych miejsc proszę przyjechać później"
    def leave_place(self,parking):
        parked = False
        for i in parking:
            if i[0]== self.registration:
                parked = True
        if parked == False:
            return "Twoje auto nie jest zaparkowane na naszym parkingu"
        parking[self.place][0]=""
        if self.buy == False:
            self.place = ""
        return "Twoje auto wyjechało. Dziękujemy za skorzystanie z naszego parkingu"
    def rejestr_car(self,car_list):
        if self.registration not in car_list:
            car_list.append(self.registration)
            return  "Twoje auto zostało zarejestrowane"
        return "Twoje auto jest już w naszy systemie"
    def find_car (self,parking):
        for i in parking:
            if self.registration == i[0]:
                return "Twoje auto znajduje się na miejscu: "+str(parking.index(i))
            return "Twoje auto nie jest zaparkowane na naszym parkingu"
cars = []
def choose_car(cars):
    for i in range (len(cars)):
        print(str(i+1)+". "+cars[i].registration)
    chosen_car = int(input("Podaj numer wybranego auta"))
    return int(chosen_car-1)
while True:
    print("///////////////////////////////")
    print("Dostępne auta:")
    for i in range (len(cars)):
        print(str(i+1)+". "+cars[i].registration)
    print("Parking:")
    print(parking)
    try: 
        choose = int(input("1-Stwórz nowe auto \n2-Zarejestruj auto na parking\n3-Wykup miejsce parkingowe \n4-Wjedź na parking \n5-Wyjedź z parkingu\n6-Znajdź auto\n7-Wyjście\n"))
    except ValueError:
        print("Podałeś niepoprawną wartość")
    if 1<choose<7 and len(cars)==0:
        print("By skorzystać z tych opcji musisz miec stworzone auto")
    elif choose == 1:
        cars.append(Car(input("Podaj numer rejestracyjny: ").upper()))
    elif choose == 2:
        print(cars[choose_car(cars)].rejestr_car(car_list))
    elif choose ==3:
        print(cars[choose_car(cars)].buy_place(parking))
    elif choose == 4:
        print(cars[choose_car(cars)].find_place(parking,car_list))
    elif choose == 5:
        print(cars[choose_car(cars)].leave_place(parking))
    elif choose == 6:
        print(cars[choose_car(cars)].find_car(parking))
    elif choose ==7:
        break
    
    else:
        print("Podałeś niepoprawną wartość")



