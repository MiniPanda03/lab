try:
    plik = open("kody.txt","x")
except FileExistsError:
    plik = open("kody.txt","w")
def sprawdzaniekodu(kod):
    if not kod[3]=="-":
        return "Niepoprawny kod pocztowy"
sprawdzaniekodu(input("Wpisz kod"))


