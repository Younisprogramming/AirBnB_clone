#!/usr/bin/python3
""" my doc class :) """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """ pycodestyle  """

    prompt = '(hbnb) '
    myclasses = ['BaseModel', 'User', 'Amenity',
            'Place', 'City', 'State', 'Review']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """ where is the doc ?! """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.myclasses:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'City': City, 'Amenity': Amenity, 'State': State,
                    'Review': Review}
            my_model = dct[arg]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ (::::) """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.myclasses:
            print("** class doesn't exist **")
            return
        if len(args) < 2 or args[1] == "":
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        obj = storage.all().get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ write anything """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.myclasses:
            print("** class doesn't exist **")
            return

        if len(args) < 2 or args[1] == "":
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        obj = storage.all().get(key)

        if obj:
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ be relax """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()

        class_name = args[0]
        if class_name not in HBNBCommand.myclasses:
            print("** class doesn't exist **")
            return
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """ you can make it """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.myclasses:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            class_name = args[0]
            instance_id = args[1]

            objects = storage.all()
            key = f"{class_name}.{instance_id}"

            if key not in objects:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            elif len(args) < 4:
                print("** value missing **")
                return

            value = args[3].replace('"', '')

            for key, objc in objects.items():
                ob_id = objc.id
                if ob_id == args[1]:
                    setattr(objc, args[2], value)
                    storage.save()
                    storage.reload()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
