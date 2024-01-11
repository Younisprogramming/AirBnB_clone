#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dictFormat = {}
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
