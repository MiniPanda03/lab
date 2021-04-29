import math
from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self,rodzaj,boki):
        self.rodzaj = rodzaj
        self.boki = boki
    @abstractmethod
    def pole(self):
        pass
    @abstractmethod
    def obwod(self):
        pass 
    def __repr__(self):
        return f"{self.rodzaj}\nObwod: {self.obwod()}\nPole: {self.pole()}"
    def __del__(self):
        print(f"{self.rodzaj} został usunięty")

class Trojkat(Figura):
    def __init__(self,bok1,bok2,bok3):
        super().__init__("Trojkat",[bok1,bok2,bok3])
    def obwod(self):
        return str(self.boki[0] + self.boki[1] + self.boki[2])
    def pole(self):
        p = float(self.obwod())/2
        pole = str(math.sqrt(p*(p-self.boki[0])*(p-self.boki[1])*(p-self.boki[2])))
        return pole
class Kolo(Figura):
    def __init__(self,promien):
        super().__init__("Koło",promien)
    def obwod(self):
        return str(2 * math.pi * self.boki)
    def pole(self):
        return str(math.pi * self.boki ** 2)
class Kwadrat(Figura):
    def __init__(self,bok1):
        super().__init__("Kwadrat",bok1)
    def obwod(self):
        return str(4 * self.boki)
    def pole(self):
        return str(self.boki ** 2)
class Prostokat(Figura):
    def __init__(self,bok1,bok2):
        super().__init__("Prostokąt",[bok1,bok2])
    def obwod(self):
        return str(2 * (self.boki[0] + self.boki[1]))
    def pole(self):
        return str(self.boki[0] * self.boki[1])
class Romb(Figura):
    def __init__(self,bok1,bok2):
        super().__init__("Romb",[bok1,bok2])
    def obwod(self):
        return 4*self.boki[0]
    def pole(self):
        return str(self.boki[0] * self.boki[1])
class Trapez(Figura):
    def __init__(self,bok1,bok2,wysokoscodboku):
        super().__init__("Trapez",[bok1,bok2,wysokoscodboku])
    def obwod(self):
        return str(2* self.boki[0]+2*self.boki[1])
    def pole(self):
        return str(self.boki[0] * self.boki[2])
figury = []
figury.append(Trojkat(5,5,5))
figury.append(Kolo(3))
figury.append(Prostokat(8,5))
figury.append(Kwadrat(9))
figury.append(Romb(4,2))
figury.append(Trapez(3,5,4))
for i in figury:
    print(i.wypisz())

