#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
	    self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
	                           .format(getenv("HBNB_MYSQL_USER"),
	                                   getenv("HBNB_MYSQL_PWD"),
	                                   getenv("HBNB_MYSQL_HOST"),
	                                   getenv("HBNB_MYSQL_DB")),
	                           		pool_pre_ping=True)

	    if getenv("HBNB_ENV") == "test":
	    	Base.metadata.drop_all()

    def all(self, cls=None):
        """ query on the current database session (self.__session)
        all objects depending of the class name (argument cls) """
        new_d = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key_id = type(obj).__name__ + '.' + obj.id
                new_d[key_id] = obj
        else:
            classes = ["State", "City", "Place", "Review", "User", "Amenity"]
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key_id = type(obj).__name__ + '.' + obj.id
                    new_d[key_id] = obj
        return new_d

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine)
        Session = scoped_session(session)
        self.__session = Session()

    def delete(self, obj=None):
        """ delete obj from the current database session """
        if obj is not None:
        	self.__session.delete(obj)
