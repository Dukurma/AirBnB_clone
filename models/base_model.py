#!/usr/bin/env python3

''' Module containing the base class of all our models '''

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    ''' Base class that all other classes inherit from '''

    def __init__(self, *args, **kwargs):
        ''' Initializes the base model '''
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        dateformat = "%Y-%m-%dT%H:%M:%S.%f"
        
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, dateformat)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, dateformat)
                elif key == "__class__":
                    pass
                else:
                    self.__dict__[key] = value

    def __str__(self):
        ''' Returns a readable form of the instance '''
        return(f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        '''Saves a newly added instance'''
        self.updated_at = datetime.today()

    def to_dict(self):
        ''' Convert an instance to a dict'''
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
