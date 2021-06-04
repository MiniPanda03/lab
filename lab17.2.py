import os 
from sqlalchemy import Column,ForeignKey,Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

if os.path.exists('test.db'):
    os.remove('test.db')
baza = create_engine('sqlite:///test.db') # ':memory:'
BazaModel=declarative_base()

class Druzyna(BazaModel):
    __tablename__ = 'druzyna'
    id =Column(Integer,primary_key=True)
    nazwa =Column(String(100),nullable=False)
    miasto =Column(String(100),nullable=False)
    ilosc = Column(Integer(50),nullable=False)
    zawodnik =relationship('Zawodnik',backref='druzyna')
    mecz =relationship('Mecz',backref='druzyna')

class Zawodnik(BazaModel):
    __tablename__ = 'zawodnik'
    id = Column(Integer,primary_key=True)
    imie= Column(String(100),nullable=False)
    nazwisko = Column(String(100),nullable=False)
    druzyna_id=Column(Integer,ForeignKey('druzyna.id'))
class Mecze(BazaModel):
    __tablename__ = 'mecz'
    id = Column(Integer,primary_key=True)
    miejsce= Column(String(100),nullable=False)
    wynikdruzyna1 = Column(Integer(100),nullable=False)
    wynikdruzyna2 = Column(Integer(100),nullable=False)
    druzyna1_id=Column(Integer,ForeignKey('druzyna.id'))
    druzyna2_id = Column(Integer, ForeignKey('druzyna.id'))

BazaModel.metadata.create_all(baza)

BDSesja=sessionmaker(bind=baza)
sesja =BDSesja()

if not sesja.query(Druzyna).count():
    sesja.add(Druzyna(nazwa='qwer', miasto='dasas',ilosc=20))
    sesja.add(Druzyna(nazwa='asdf', miasto='dsdax',ilosc=25))
if not sesja.query(Mecze).count():
    sesja.add(Mecze(miejsce='dsaasd',wynikdruzyna1=1,wynikdruzyna2=4,druzyna1_id=1,druzyna2_id=2))
def czytajdane():
    for mecz in sesja.query(Mecze).join(Druzyna).all():
        print(mecz.id,mecz.miejsce,mecz.wynikdruzyna1,mecz.wynikdruzyna2,mecz.druzyna1_id.nazwa,mecz.druzyna2_id.nazwa)
czytajdane()

sesja.commit()