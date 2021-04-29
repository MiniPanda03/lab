from abc import ABC, abstractmethod
import time

class Restaurant(ABC):
    def __init__(self,name,place,flavor):
        self.name = name
        self.place = place
        self.flavor = flavor


    def next(self):
        print("Dostępne smaki:")
        for i in range (len(self.flavor)):
            print(str(i+1)+self.flavor[i])
    @abstractmethod
    def make(self):
        pass
class IceCreamStand(Restaurant):
    def __init__(self,name,place,flavor,priceforscoop):
        super().__init__(name,place,flavor)
        self.priceforscoop = priceforscoop

    def make(self):
        galki = []
        print(f"Witamy w lodziarni {self.name}")
        ilosc = int(input("Ile gałek chcesz kupić?"))
        print(self.next())
        for i in range(ilosc):
            galki.append(input(f"Wybierz {i+1} gałke"))
        opakowanie = input("Chcesz lody w wafelku czy w podełku?")
        print(f"Oto twoje lody w {opakowanie} z gałkami po kolei: ",end="")
        for i in galki:
            print(i,end=',')
        return f"Musisz zapłacić {ilosc*self.priceforscoop}"
        

class CoffeeShop(Restaurant):
    def __init__(self,name,place,flavor):
        super().__init__(name,place,flavor)
    def make(self):
        print(f"Witamy w kawiarni {self.name}")
        print(self.next())
        wybor = int(input("Wybierz kawe i podaj jej numer"))
        print(f"Poczekaj aż zrobimy twoje {self.flavor[wybor]}")
        time.sleep(3)
        return f"Prosze bardzo, oto twoje {self.flavor[wybor]}"

caffe = ["latte","americano","espresso","capuccino"]
lodziarnia = IceCreamStand("Yup","Wasada 12",["Czek","smiet","trus","cytr"],6)
kawa = CoffeeShop("sas","asasa 2",caffe)
print(kawa.make())
print(lodziarnia.make())

        
        
