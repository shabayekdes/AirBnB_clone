#!/usr/bin/env python3
""" Main script for the HBnB console.
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ HBnBCommand class defines a command-line 
    interpreter for object management and storage.
    """

    my_models = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}

    prompt = "(hbnb) "
    models = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"]

    def do_quit(self, args):
        """ Quit command to exit the program.\n
        """
        quit()

    def do_EOF(self, args):
        """ End Of File command to exit the program.\n
        """
        quit()

    def emptyline(self):
        """ Do nothing on empty line\n
        """
        pass

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""

        all_data = storage.all()
        my_data = []
        if args not in HBNBCommand.my_models:
            print("** class doesn't exist **")
            return
        if args in self.models:
            for key, value in all_data.items():
                if args in key:
                    split_str = key.split(".")
                    new_str = "[" + split_str[0] + "]"\
                        + " (" + split_str[1] + ")"
                    my_data.append(new_str + " " + str(value))
                    print(my_data)

    def do_show(self, args):
        """ Print the string representation of an instance.
        """
        if not args:
            print("** class name missing **")
            return
        
        args_split = shlex.split(args)
        if args_split[0] not in HBNBCommand.my_models:
            print("** class doesn't exist **")
            return
        elif len(args_split) == 1:
            print("** instance id missing **")
            return
        my_data = storage.all()
        new_object = "{}.{}".format(args_split[0], args_split[1])
        if new_object not in my_data.keys():
            print("** no instance found **")
            return
        else:
            print("{}".format(my_data[new_object]))

    def do_create(self, args):
        """ Create a new instance of a specified class.
        """
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.my_models:
            print("** class doesn't exist **")
            return
        else:
            new_object = eval(args[0])()
            new_object.save()
            print(new_object.id)

    def do_update(self, args):
        """ Update an instance based on the class name.
        """
        args_split = shlex.split(args)
        if len(args_split) < 4:
            print("Usage: update <class name> <id> <attribute name> \"<attribute value>\"")
            return
        
        model_name, instance_id, attribute, value = args_split[:4]

        if model_name not in HBNBCommand.models:
            print("** class doesn't exist **")
            return
        
        instance_key = "{}.{}".format(model_name, instance_id)

        if instance_key not in storage.all():
            print("** no instance found **")
            return
        
        if attribute in ["id", "created_at", "updated_at"]:
            print("** cannot update '{}' attribute **".format(attribute))
            return
        instance = storage.all()[instance_key]

        if not hasattr(instance, attribute):
            print("** attribute name missing **")
            return
        
        if not isinstance(getattr(instance, attribute), (str, int, float)):
            print("** only 'simple' attributes can be updated: string, integer, and float **")
            return
        
        try:
            setattr(instance, attribute, type(getattr(instance, attribute))(value))
            storage.save()
            print("Update successful for {}: {}.".format(instance_key, attribute))
        except ValueError:
            print("** invalid value for '{}' attribute type **".format(attribute))
        
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args_split = shlex.split(args)
        if len(args_split) == 0:
            print("** class name missing **")
            return

        class_name = args_split[0]
        if class_name not in HBNBCommand.models:
            print("** class doesn't exist **")
            return

        if len(args_split) > 1:
            instance_id = args_split[1]

            instance_key = "{}.{}".format(class_name, instance_id)
            if instance_key in storage.all():
                del storage.all()[instance_key]

                storage.save()
                print("Instance {} deleted.".format(instance_key))
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_count(self, args):
        """ Count the number of instances of a class.
        """
        args_split = shlex.split(args)
        count = 0
        for obj in storage.all().values():
            if args_split[0] == obj.__class__.__name__:
                count += 1
        print(count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
