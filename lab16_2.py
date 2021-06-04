import sqlite3

con= sqlite3.connect('baza.db')

con.row_factory = sqlite3.Row
cur= con.cursor()

create_table = """ CREATE TABLE IF NOT EXISTS praca (id integer PRIMARY KEY, name text NOT NULL, surname text NOT NULL, place text NOT NULL, ernings int NOT NULL); """

def add_person():
    cur.execute('INSERT INTO praca VALUES(NULL, ?, ?);', (input("Podaj imie"), input("Podaj nazwisko"),))
def del_person():
    name = input("Podaj imie")
    surname = input("Podaj nazwisko")
    cur.execute('DELETE FROM praca WHERE name = ? AND surname = ? ', (name, surname,))
def sort_by_name():
    cur.execute('SELECT * FROM praca ORDER BY name ASC')
    tab = cur.fetchall()
    for i in tab:
        print(i['id'],i['name'],i['surname'],i['place'],i['ernings'])
def change():
    cur.execute('UPDATE praca SET surname = ?, ernings = ?, place = ? WHERE id = ?;',(input("Podaj nazwisko"),int(input("Podaj zarobki")),input("Podaj miasto")))
def take_max_earn():
    cur.execute('SELECT name, surname,place, MAX(ernings) FROM praca')
    max = cur.fetchall()
    for i in max:
        print(i['id'], i['name'], i['surname'], i['place'], i['ernings'])
def take_min_earn():
    cur.execute('SELECT name, surname,place, MIN(ernings) FROM praca')
    mini = cur.fetchall()
    for i in mini:
        print(i['id'], i['name'], i['surname'], i['place'], i['ernings'])