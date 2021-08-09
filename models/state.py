#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from models import storage

class State(BaseModel):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    @property
    def cities(self):
    	list = []
    	print(storage.all(City))
    	print("HERE")
