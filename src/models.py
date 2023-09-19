import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250) , nullable=False)
    rotation_period = Column(String(250) , nullable=False)
    orbital_period = Column(String(250) , nullable=False)
    gravity = Column(String(250) , nullable=False)
    surface_water = Column(String(250) , nullable=False)
    diameter = Column(String(250) , nullable=False)
   



class Characters(Base):
    __tablename__ = 'characters'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(250) , nullable=False)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    description = Column(String(250))
    gender = Column(String(250))
    eye_color = Column(String(250))
    height = Column(Integer, nullable = False)
    age = Column(Integer, nullable = False)
   
    

class Starships(Base):
    __tablename__ = 'starships'
    
    id = Column(Integer, primary_key=True)
    model = Column(String(250) , nullable=False)
    starship_class = Column(String(250) , nullable = False)
    capacity = Column(Integer)
    speed = Column(Integer, nullable = False)
    length = Column(Integer, nullable = False)
    weight = Column(Integer, nullable = False)
    


class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(Users)
    
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship(Planets)

    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship(Characters)

    starships_id = Column(Integer, ForeignKey('starships.id'))
    starship = relationship(Starships)

render_er(Base, 'diagram.png')
