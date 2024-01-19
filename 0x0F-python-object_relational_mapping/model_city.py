#!/usr/bin/python3
"""Module of the city class"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    '''Base Class of cities'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
