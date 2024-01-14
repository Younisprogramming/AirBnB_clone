#!/usr/bin/python3
""" my doc class :) kso gtpsrk htgswtrh
hrt rth det"""
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
myclasses = [
        'BaseModel',
        'User',
        'Amenity',
        'Place',
        'City',
        'State',
        'Review'
        ]


class HBNBCommand(cmd.Cmd):
    """ pycodestyle  spork hypoyks hpokrys hr
    okmyi resoimhyo6"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program sektygra5t hy
         srht srt hy6rsety"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the programa 5yoie4wj5oij y54owijy 5w4
        w54ey gsr6y """
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line se y5h44ewa y54
         ytwr yh6wt4s y"""
        pass

    def do_create(self, arg):
        """ where is the doc ?! ws ty er6 uhyet5d6y hj
         6ywr ys6rw y6e56 """
        if not arg:
            print("** class name missing **")
        elif arg not in myclasses:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[arg]()
            print(my_model.id)
            my_model.save()

    def do_show(self, arg):
        """ (::::) tr4 hyoirwsth iksr hywry h
         wrhys w6 hyedt6 ye6 yr"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in myclasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ write anything rstlkhywy6 twr6 yw ry6w 6ry4
         6ywr w6yr 6yrw y6wr"""
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in myclasses:
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
        """ be relax swy twry 5w64y 4q6wu56uau
         wu5yallky5lloyws;pyr6dl """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()

        class_name = args[0]
        if class_name not in myclasses:
            print("** class doesn't exist **")
            return
        else:
            obj_list = [
                    obj.__str__() for obj in storage.all().values()
                    if obj.__class__.__name__ == class_name
                    ]
        if obj_list:
            print(obj_list)
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """ you can make it kjlaet uji s5teuk srtio
        lkstrhjksrt kj   kjsthrkj trs5"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in myclasses:
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
