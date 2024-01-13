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
mylist = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    """ pycodestyle  """

    prompt = '(hbnb) '

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
            return
        elif arg not in mylist:
            print("** class doesn't exist **")
        else:
            new_inst = mylist[arg]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """ (::::) """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in mylist:
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
        if class_name not in mylist:
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
        if class_name not in mylist:
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
        if not arg:
            print("** class name missing **")
            return
        combined_args = ""
        for argv in arg.split(','):
            combined_args = combined_args + argv
            args = shlex.split(combined_args)
            if args[0] not in mylist:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                all_objects = storage.all()
                for key, current_object in all_objects.items():
                    obj_name = current_object.__class__.__name__
                    obj_id = current_object.id
                    if obj_name == args[0] and obj_id == args[1].strip('"'):
                        if len(args) == 2:
                            print("** attribute name missing **")
                        elif len(args) == 3:
                            print("** value missing **")
                        else:
                            setattr(current_object, args[2], args[3])
                            storage.save()
                            return
                        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
