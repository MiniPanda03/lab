try:
    tekst=open('news.txt','r')
except FileExistsError:
    tekst=open(input("Podaj nazwe pliku"),'r')
try:
    tekst2=open('news2.txt', 'r')
except FileExistsError:
    tekst2=open(input("Podaj nazwe pliku"),'r')

tab = tekst.readlines()
tab2 = tekst2.readlines()
zapis = open("tekst.txt","w")
if len(tab)>len(tab2):
    for i in range(len(tab2)):
        print(tab[i],end="")
        zapis.write(tab[i])
        print(tab2[i],end="")
        zapis.write(tab2[i])
else:
    for i in range(len(tab)):
        print(tab[i],end="")
        zapis.write(tab[i])
        print(tab2[i],end="")
        zapis.write(tab2[i])
