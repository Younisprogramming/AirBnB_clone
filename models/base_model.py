#!/usr/bin/python3
"""This is the base class for all models."""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is the base class for all models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the Bas
        eModel class.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(
                kwargs.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                kwargs.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the print/str representation of the
        BaseModel instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """Save the BaseModel instance.
        mare talk talk
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert the BaseModel instance to a d
        dict: A dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
