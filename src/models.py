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

    def log_in():
        print("Logged In")

    def sign_in():
        print("Signed In")

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250) , nullable=False)
    size = Column(String(250) , nullable=False)
    population = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(250) , nullable=False)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    height = Column(Integer, nullable = False)
    age = Column(Integer, nullable = False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    model = Column(String(250) , nullable=False)
    manufacturer = Column(String(250) , nullable = False)
    capacity = Column(Integer)
    speed = Column(Integer, nullable = False)
    weight = Column(Integer, nullable = False)

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    users = relationship(Users)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planets = relationship(Planets)
    character_id = Column(Integer, ForeignKey('character.id'))
    characters = relationship(Characters)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicles = relationship(Vehicles)

render_er(Base, 'diagram.png')
