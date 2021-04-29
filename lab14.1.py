class Pojazd:
    def __init__(self,rodzaj,nr_tablica):
        self.nr_tablica = nr_tablica
        self.rodzaj = rodzaj
    def wyswietl_tablice(self):
        return f"Twoj {self.rodzaj} ma rejestracje: {self.nr_tablica}"
    
    
    def __del__(self):
        print(f"{self.rodzaj} został usunięty".upper())
    
class Samochod(Pojazd):
    def __init__(self,nr_tablica):
        super().__init__("samochód",nr_tablica)

class Motocykl(Pojazd):
    def __init__(self,nr_tablica):
        super().__init__("motor",nr_tablica)

auto = Samochod("DWR12345")
motor = Motocykl("WW453QAS")

print(auto.wyswietl_tablice())
print(motor.wyswietl_tablice())

