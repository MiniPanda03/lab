import  pytest


def bmr(plec,masa,wiek,wzrost,aktywnosc):
    aktywnosci = {
        "brak": 1.2,
        "niskie": 1.3,
        "srednie": 1.5,
        "wysokie": 1.7,
        "bardzo wysokie": 1.9
    }
    print(type(masa))
    print(type(wiek))
    print(type(wzrost))
    oblicz = (masa*9.99)+(wzrost*6.25)-(wiek*4.92)
    if plec =="F":
        return round((oblicz-161)*aktywnosci[aktywnosc],0)
    elif plec == "M":
        return  round((oblicz+5)*aktywnosci[aktywnosc],0)
    else:
        return  False

def test_bmr():
    assert bmr("F",40,18,160,"niskie") == 1495.0
    assert bmr("M",80,24,180,"wysokie") == 3079.0
    assert bmr("F",50,30,170,"srednie") == 1890.0



#[9,99 x masa ciała (kg)] + [6,25 x wzrost (cm)] - [4,92 x wiek(lata)] - 161
#[9,99 x masa ciała (kg)] + [6,25 x wzrost (cm)] - [4,92 x wiek (lata)] + 5