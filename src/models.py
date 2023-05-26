import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
   
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id =Column(Integer, primary_key=True) 
    name =Column(String(50))
    apellido=Column(String(50)) 
    email =Column(String(50)) 
    password = Column(String(20)) 
    edad = Column(Integer) 
    
class Personajes(Base):
    __tablename__ ="personajes"   
    id =Column(Integer, primary_key=True) 
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    

class Planets(Base):
    __tablename__= "planets"  
    id =Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)

class Fav_Planets(Base):
    __tablename__= "fav_planets"  
    id = Column(Integer, primary_key=True)
    favoritos =Column (Integer,ForeignKey("Planets.id") )
    favoritos_planets = Column(Integer, ForeignKey("planets.id"))
    user_like = Column (Integer, ForeignKey("usuario.id"))

class Fav_Persons(Base):
    __tablename__= "fav_persons"  
    id = Column(Integer, primary_key=True)
    favoritos =Column (Integer,ForeignKey("personajes.id"))
    user_like = Column (Integer, ForeignKey("usuario.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
