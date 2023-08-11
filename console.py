#!/usr/bin/python3
"""
doc
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    doc
    """
    prompt = "(hbnb) "
    classes = ("BaseModel",)

    def do_quit(self, arg):
        """
        doc
        """
        return True

    def do_EOF(self, arg):
        """
        doc
        """
        return True

    def do_emptyline(self, arg):
        """
        doc
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
