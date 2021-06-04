import pytest

def paliondrom(tekst):
    for i in range (len(tekst)):
        if tekst[i]==tekst[len(tekst)-i-1]:
            continue
        else:
            return False
    return True


def test_paliondrom():
    assert paliondrom("anna") == True
    assert paliondrom("oko") == True
    assert paliondrom("test") == False
