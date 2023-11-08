#!/usr/bin/env python3
"""
Console for object management and storage
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program.\n"""
        quit()

    def do_EOF(self, args):
        """End Of File command to exit the program"""
        quit()

    def emptyline(self):
        """Do nothing on empty line\n"""
        pass

    def do_create(self, args):
        """Create a new instance"""
        print("Create ...!")
        pass

    def do_show(self, args):
        """Prints the string representation of an instance."""
        print("Show ...!")
        pass

    def do_destroy(self, args):
        """Deletes an instance."""
        print("Delete ...!")
        pass

    def do_all(self, args):
        """Prints all string representation of all instances"""
        print("Get All ...!")
        pass

    def do_update(self, args):
        """Updates an instance based on the class name."""
        print("Update ...!")
        pass

    def do_count(self, args):
        """Counts the number of instances of a class"""
        print("Count ...!")
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
