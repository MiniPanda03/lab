def miesiac():
    miesiac= ["styczen","luty","marzec","kwiecien","maj","czerwiec","lipiec","sierpien","wrzesien","pazdziernik","listopad","grudzien"]
    i = int(input("Podaj liczbe"))
    if i>12 or i<=0:
        print("Podaj poprawną liczbę")
    else:
        print(miesiac[i-1])
miesiac()