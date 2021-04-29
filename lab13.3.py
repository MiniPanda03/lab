class Smartphone:
    def __init__(self,color,camera,cpu,os,battery,price,manufacturer,model,memory):
        self.color = color
        self.camera = camera
        self.cpu = cpu
        self.os = os
        self.battery = battery
        self.price = price
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.taken = 0
        self.app = [["Zdjęcia",0]]
    def __repr__(self):
        return "CPU: {}\nOS: {}\nProducent: {}\nModel: {}\nPamięć: {}".format(self.cpu,self.os,self.manufacturer,self.model,self.memory)
    def battery_charge (self):
        if self.battery < 3:
            print("Twoja bateria ma {} %, telefon zostaje wyłączony".format(self.battery))
        elif self.battery < 20:
            print("Twoja bateria ma {} %, musisz ją podładować".format(self.battery))
        else:
            print("Twoja bateria ma {} %".format(self.battery))
        if input("Czy chcesz podładować? T/N: ").upper().strip() == "T" and self.battery < 100:
                while self.battery<100:
                    self.battery +=1
                    print("Naładowanie {}".format(self.battery))
                return "Bateria została naładowana"
    def add_app(self,name,place):
        if self.taken+place>self.memory:
            return "Nie możesz instalować więcej aplikacji, usuń coś"
        self.taken = self.taken+ place
        self.app.append([name,place])
        return "Dodano aplikacje"
    def remove_app(self):
        licz = 1
        for i in self.app:
            print("{}. Nazwa: {}, ile zajmuje {}".format(licz,i[0],i[1]))
            licz+=1
        wybor = int(input("Którą aplikacje chcesz usunąć?"))
        if wybor == 1:
            return "Nie możesz usunąć tej aplikacji"
        self.taken = self.taken - self.app[wybor-1][1]
        self.app.pop(wybor-1)
        return "Aplikacja została usunięta"
    def take_photo(self,bajts):
        if self.taken+bajts>self.memory:
            return "Nie ma miejsca na nowe zdjecie, usun aplikacje lub usun zdjecia"
        self.taken = self.taken+bajts
        self.app[0][1]=self.app[0][1]+bajts
        return "Zdjęcie zostało zrobione twoją kamerą {}".format(self.camera)
    def show_apps(self):
        for i in self.app:
            print("Nazwa aplikacji {}, ile zajmuje: {}".format(i[0],str(i[1])))
            

tele = Smartphone("czerwony","12 Mpix","Apple A13 Bionic","iOS 13",50,4000,"apple","Iphone se",65536)

print(tele.show_spec())
print(tele.battery_charge())
tele.show_apps()
print(tele.add_app("Reditt",1000))
print(tele.remove_app())
print(tele.take_photo(500))
tele.show_apps()
