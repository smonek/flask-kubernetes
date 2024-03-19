import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(50))
    def __repr__(self):
        return self.name


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class vyrobce(Model):
    id = Column(Integer, primary_key=True)
    vyrobce_vozidla = Column(String(50))
    def __repr__(self):
        return self.vyrobce_vozidla
        
class typ_vozidla(Model):
    id = Column(Integer, primary_key=True)
    vyrobce_vozidla = Column(String(50))
    vyrobce_id = Column(Integer, ForeignKey("vyrobce.id"), nullable=False)
    vyrobce = relationship("vyrobce")
    def __repr__(self):
        return self.vyrobce_vozidla

class rodic(Model):
    id = Column(Integer, primary_key=True)
    jmeno = Column(String(50))
    prijmeni = Column(String(50))
    def __repr__(self):
        return self.jmeno
    
class dite(Model):
    id = Column(Integer, primary_key=True)
    jmeno = Column(String(50))
    prijmeni = Column(String(50))
    rodic_id = Column(Integer, ForeignKey("rodic.id"), nullable=False)
    rodic = relationship("rodic")
    def __repr__(self):
        return self.jmeno
    
class vyrobek(Model):
    id = Column(Integer, primary_key=True)
    nazev = Column(String(70))
    sn = Column(Integer, nullable=False)
    def __repr__(self):
        return self.nazev

class sklad(Model):
    id = Column(Integer, primary_key=True)
    vyrobek_id = Column(Integer, ForeignKey("vyrobek.id"), nullable=False)
    vyrobek = relationship("vyrobek")
    datum = Column(Date)
    pocet_kusu = Column(Integer)
    stav = Column(Enum('Nakup','Prodej'), nullable=False)
    def __repr__(self):
        return self.stav


class Contact(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    address = Column(String(564))
    birthday = Column(Date, nullable=True)
    personal_phone = Column(String(20))
    personal_celphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey("contact_group.id"), nullable=False)
    contact_group = relationship("ContactGroup")
    gender_id = Column(Integer, ForeignKey("gender.id"), nullable=False)
    gender = relationship("Gender")

    def __repr__(self):
        return self.name

    def month_year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, 1, 1)
