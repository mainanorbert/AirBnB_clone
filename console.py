#!/usr/bin/python3
"""module that implements entry point for command interpreter"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
# importinng abstract syntax tree
import ast


def split_arg(command_args):
    """splits arg into array of args"""
    # del_expression = r'[ ,\t]+'
    # split_args = re.split(del_expression, command_args)
    # args = [my_arg for my_arg in split_args]
    args = command_args.split()
    return args


class HBNBCommand(cmd.Cmd):
    """class that implements entry point for cmd interpreter
    Args:
    cmd_prompt (str): display for user
    my_classes"""
    prompt = "(hbnb) "
    __my_classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review",
            }

    def do_quit(self, arg):
        """Quits this program by typing 'quit + ENTER'"""
        return True

    def do_EOF(self, args):
        """implementing ctrl+ D end of file"""
        print()
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """creates and stores a class
        Usege: create <Class Name>"""
        args = split_arg(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """prints str rep of objs based on cls name
        Usage: show <Class Name> <object id>"""
        args = split_arg(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            if f"{args[0]}.{args[1]}" not in storage.all().keys():
                print("** no instance found **")
            else:
                key = f"{args[0]}.{args[1]}"
                objs = storage.all()[key]
                print(objs)

    def do_destroy(self, arg):
        """deleting an instance based on class name and id
        Usage: destroy <Class name> <instance_id>"""
        args = split_arg(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist ** ")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """prints all str rep of instances in list form
        Usage: all or all <class name>"""
        args = split_arg(arg)
        my_objs = []
        if len(args) == 0:
            for obj in storage.all().values():
                my_objs.append(obj.__str__())
                print(my_objs)
        elif len(args) != 0 and args[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if k.startswith(args[0]):
                    my_objs.append(v.__str__())
                    print(my_objs)

    def do_update(self, arg):
        """updates instance based on id
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        args = split_arg(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = storage.all()[key]
            try:
                setattr(obj, args[2], args[3])
                storage.save()
            except ValueError:
                pass

    def default(self, arg):
        """retrieving number of objsc of class
        Usage <class>.count()"""
        args = arg.split('.')
        if len(args) == 1:
            print("unknown")
        elif len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                no_of_objs = 0
                for k, v in storage.all().items():
                    if k.startswith(args[0]):
                        no_of_objs += 1
                print(no_of_objs)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
