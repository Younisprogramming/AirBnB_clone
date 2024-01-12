#!/usr/bin/python3
import json
import os
""" class doc .."""


class FileStorage:
    """ storage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all func."""
        return FileStorage.__objects

    def new(self, obj):
        """new func."""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """save func."""
        dictObj = {}

        for key, val in FileStorage.__objects.items():
            dictObj[key] = val.to_dict()
            dictObj[key]['__class__'] = val.__class__.__name__
        with open(FileStorage.__file_path, "w") as jsonFile:
            json.dump(dictObj, jsonFile)

    def reload(self):
        """ Deserializes __objects from the JSON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City,
               'Amenity': Amenity, ' Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as filejs:
                for key, value in json.load(filejs).items():
                    self.new(dct[value['__class__']](**value))
