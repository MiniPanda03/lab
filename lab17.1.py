from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String



engine = create_engine('sqlite:///movie.db', echo = True)
meta = MetaData()

movie = Table(
   'movie', meta,
   Column('id', Integer, primary_key = True), 
   Column('nazwa', String), 
   Column('rezyser', String),
   Column('aktorzy',String),
   Column('ocena',Integer),
   Column('gdzieogladac',String),
)
meta.create_all(engine)
conn = engine.connect()
def delete_movie():
   usun = movie.delete().where(movie.c.nazwa == input("Podaj nazwe filmu które chcesz usunąć: "))
   conn.execute(usun)
def add_movie():
   ins = movie.insert().values(nazwa=input("Podaj nazwe: "), rezyser=input("Podaj reżysera: "), aktorzy=input("Podaj aktorów"),ocena=input("Podaj ocene"),gdzieogladac=input("Gdzie oglądać? "))
   result = conn.execute(ins)
def change_movie():
   zmien = movie.update().where(movie.c.nazwa == input("Podaj nazwe filmu którego chcesz zmienić: ")).values(rezyser=input("Podaj reżysera: "), aktorzy=input("Podaj aktorów"),ocena=input("Podaj ocene"),gdzieogladac=input("Gdzie oglądać? "))
   conn.execute(zmien)
def show_data():
   chose = movie.select()
   conn.execute(chose).fetchall()
add_movie()
show_data()