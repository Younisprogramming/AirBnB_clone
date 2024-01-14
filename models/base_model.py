#!/usr/bin/python3
"""This is the base class for all models."""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is the base class for all models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
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
        """returns class name, id and attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)


    def save(self):
        """Save the BaseModel instance.
        mare talk talk
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
