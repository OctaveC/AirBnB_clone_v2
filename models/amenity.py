#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.schema import Column
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Amenity(BaseModel, Base):
    """ class Amenity """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
