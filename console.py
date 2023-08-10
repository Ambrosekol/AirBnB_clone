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
    prompt = "(hbnb)"
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

    def do_create(self, arg):
        """
        doc
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg.strip() in HBNBCommand.classes:
            obj = eval(arg.strip())()
            storage.new(obj)
            storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")


    def do_all(self, arg):
        """
        doc
        """
        my_list = []
        args = arg.split()
        if len(args) >= 1:
            if args[0] in HBNBCommand.classes:
                key = args[0] 
                for k,v in storage.all().items():
                    if k.startswith(key):
                        my_list.append(v)
                print(my_list)
            else:
                print("** class doesn't exist **")
                return
        if len(args) == 0:
            for values in storage.all().values():
                my_list.append(values)
            print(my_list)

    def do_show(self, arg):
        """
        doc
        """
        args = arg.split()
        if len(args) >= 2:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                    return
                else:
                   print( storage.all().get(key))
                   return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 0:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        doc
        """
        args = arg.split()
        if len(args) >= 2:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            else:
                key = args[0] + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                    return
                else:
                    del(storage.all()[key])
                    return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 0:
            print("** class name missing **")
            return

    def do_update(self, arg):
        """
        doc
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
