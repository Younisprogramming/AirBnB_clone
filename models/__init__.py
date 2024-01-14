""" Import modules and packages """
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
