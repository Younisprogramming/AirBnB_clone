#!/usr/bin/python3
"""
Parent class that will inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """wte gwt hyw4 ty
     w6hr hwry whr t"""

    def __init__(self, *args, **kwargs):
        """ e56hrw 56hye 5hyw5 6e"""
        if kwargs:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """ 5e6h e5h w56h e5wwwhyw6ww6y"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ e5h hyet6 hye5yh e5t yh"""
        dictFormat = {}
        for key, val in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict

    def __str__(self):
        """ e56 hye56 yh5e hy5e h6e5 6e5h"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
