#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ Trucnboiduche """
            list = []
            print(storage.all(City))
            for city in cities:
                if city.state_id == self.id:
                    list.append(city)
            return list
