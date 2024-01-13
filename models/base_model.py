#!/usr/bin/python3
"""Module for BaseModel"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """Base class for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, f)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        dict_format = {}
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dict_format[key] = val.isoformat()
            else:
                dict_format[key] = val
        return dict_format

    def __str__(self):
        """Return a string representation of the instance"""
        cl = self.__class__.__name__
        return f"[{cl}] ({self.id}) {self.__dict__}"
