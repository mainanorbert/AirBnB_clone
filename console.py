#!/usr/bin/python3
"""module that implements entry point for command interpreter"""
import cmd
import re
from models import storage
from models.base_model import BaseModel


def split_arg(command_args):
    """splits arg into array of args"""
    # del_expression = r'[ ,\t]+'
    # split_args = re.split(del_expression, command_args)
    # args = [my_arg for my_arg in split_args]
    args = command_args.split()
    return args


class HBNBCommand(cmd.Cmd):
    """class that implements entry point for cmd interpreter"""
    cmd_prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quits this program by typing 'quit + ENTER'"""
        return True

    def do_EOF(self, args):
        """implementing ctrl+ D end of file"""
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
        elif args[0] != "BaseModel":
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
        elif args[0] != "BaseModel":
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
        elif args[0] != "BaseModel":
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
        if len(args) != 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_objs = []
            for objs in storage.all().values():
                if len(args) > 0 and args[0] == "BaseModel":
                    my_objs.append(objs.__str__())
                else:
                    my_objs.append(objs.__str__())
            print(my_objs)

    def do_update(self, arg):
        """updates instance based on id
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        args = split_arg(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
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
            obj_dict = storage.all()[key]
            if args[2] in obj_dict.__class__.__dict__.keys():
                value_type = type(obj_dict.__class__.__dict__[args[2]])
                obj_dict.__dict__[args[2]] = value_type(args[3])
            else:
                obj_dict.__dict__[args[2]] = args[3]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
