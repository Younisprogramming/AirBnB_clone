#!/usr/bin/python3
""" yjetd yhwr uhteyd ujsyt uj
 dty jdt yjutd"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """wr6y hety huesry twr6 yer6y 
     rt hyywr hy"""

    def __init__(self, *args, **kwargs):
        """ ywerh  6ywr4 y65wu w65 u w46ry 4"""
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
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ yw4 y6wr 6w5 yu5e6u w5r6yu w56 u"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ 6y4w yw56uy w64r yue5r6yu e56hy u"""
        dictFormat = {}
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dictFormat[key] = val.isoformat()
            else:
                dictFormat[key] = val
        return dictFormat

    def __str__(self):
        """ 64w yuw6r uw56u w56u 64 """
        cl = self.__class__.__name__
        return "[{}] ({}) {}".format(cl, self.id, self.__dict__)
