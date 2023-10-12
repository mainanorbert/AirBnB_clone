#!/usr/bin/python3
"""module that implements entry point for command interpreter"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
