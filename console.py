#!/usr/bin/python3
"""Create the AirBnB  console."""

import cmd
import json
import re
from shlex import split
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    classes = {"BaseModel", "FileStorage", "User", "State",
            "City", "Amenity", "Place", "Review"}

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, args):
        """ Creates a new instance """
        if not (args):
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval[args]()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ Prints str representation of an instance """
        if not (args):
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for k, v in storage.all().items():
                    if args[1] == v.id:
                        print(v)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, args):
        """ Prints all str representation of all instances """
        split_args = split(args)
        n_list = []
        dict_json = models.storage.all()
        if args:
            try:
                for key in models.storage.all():
                    if split_args[0] == key.split('.')[0]:
                        n_list.append(str(dict_json[key]))
                print(n_list)
            except Exception:
                print("** class doesn't exist **")
        else:
            for key in models.storage.all():
                n_list.append(str(models.storage.all()[key]))
            print(n_list)

    def do_update(self, args):
        """ Updates an instance based on the class name and id """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in HBNBCommand.__classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
