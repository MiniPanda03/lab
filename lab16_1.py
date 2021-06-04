import sqlite3

con= sqlite3.connect('baza.db')

con.row_factory = sqlite3.Row
cur= con.cursor()

create_table = """ CREATE TABLE IF NOT EXISTS osoba (id integer PRIMARY KEY, name text NOT NULL, surname text); """
create_table = """ CREATE TABLE IF NOT EXISTS numer (id integer PRIMARY KEY, numer text NOT NULL,osoba_id INTEGER NOT NULL, FOREIGN KEY(osoba_id) REFERENCES osoba(id)); """
cur.execute(create_table)
def add_person():
    cur.execute('INSERT INTO osoba VALUES(NULL, ?, ?);', (input("Podaj imie"), input("Podaj nazwisko")))
def add_number():
    with con:
        cur.execute('SELECT * FROM osoba')
        ludzie = cur.fetchall()
        print("Osoby:")
        for i in ludzie:
            print(i['id'], i['name'], i['surname'])
    cur.execute('INSERT INTO numer VALUES(NULL, ?, ?);', (input("Podaj numer"), int(input("Podaj numer osoby"))))
def data():
    with con:
        cur.execute('SELECT * FROM osoba')
        ludzie = cur.fetchall()
        print("Osoby:")
        for i in ludzie:
            print(i['id'],i['name'],i['surname'])
        cur.execute('SELECT * FROM numer')
        numer = cur.fetchall()
        print("Numery:")
        for x in numer:
            print(x['id'],x['numer'],x['osoba_id'])
def del_number():
    with con:
        id = int(input("Podaj numer numeru ktory chcesz usunąć: "))
        cur.execute('DELETE FROM numer WHERE id=?', (id,))
    print("Usunięto numer")
def del_osoba():
    with con:
        wybrane = int(input("Wybierz osobe którą chcesz usunąć (podaj id)"))
        cur.execute('DELETE FROM numer WHERE osoba_id=?',(wybrane,))
        cur.execute('DELETE FROM osoba WHERE id=?',(wybrane,))
    print("Osoba została usunięta wraz z numerami")
def wysz_po_num():
    with con:
        numer = input("podaj numer który chcesz sprawdzić")
        cur.execute('SELECT osoba_id FROM numer WHERE numer=?', (numer,))
        osoba = cur.fetchone()
        osoba = osoba[0]
        print(osoba)
        cur.execute('SELECT * FROM osoba WHERE id = ?',(osoba,))
        ludzie = cur.fetchall()
        for x in ludzie:
            print(x['id'],x['name'],x['surname'])
def wysz_po_osobie():
    with con:
        imie = input("Podaj imie osoby")
        nazwisko = input("Podaj nazwisko")
        cur.execute('SELECT id FROM osoba WHERE name= ? AND surname = ?',(imie,nazwisko,))
        id = cur.fetchone()
        id = id[0]
        cur.execute('SELECT * FROM numer WHERE osoba_id=?',(id,))
        numery = cur.fetchall()
        for x in numery:
            print(x['id'],x['numer'])
data()
wysz_po_osobie()
