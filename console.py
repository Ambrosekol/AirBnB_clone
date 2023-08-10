#!/usr/bin/python3
"""
doc
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    doc
    """
    prompt = "(hbnb)"

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
