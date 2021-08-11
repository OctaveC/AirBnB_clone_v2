#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """ Getter attribute -> Relationship
                between State and City for FileStorage """
            list = []
            for city in len(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list.append(city)
            return list
