#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """MySQL database"""
    __engi = None
    __seion = None

    def __init__(self):
        """DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engi = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engi)

    def all(self, cls=None):
        """database session"""
        ndict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__seion.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    ndict[key] = obj
        return (ndict)

    def new(self, obj):
        """current database"""
        self.__seion.add(obj)

    def save(self):
        """commit changes"""
        self.__seion.commit()

    def delete(self, obj=None):
        """delete from database session """
        if obj is not None:
            self.__seion.delete(obj)

    def reload(self):
        """reloads"""
        Base.metadata.create_all(self.__engi)
        se_factory = sessionmaker(bind=self.__engi, expire_on_commit=False)
        Session = scoped_session(se_factory)
        self.__seion = Session

    def close(self):
        """call remove()"""
        self.__seion.remove()
