#!/usr/bin/python3
''' Module contains the entry point of the command interpreter '''
import cmd
from types import new_class
from models import hbnb_classes, storage


''' REMEMBER TO DELETE MESSAGES '''


class HBNBCommand(cmd.Cmd):
    ''' Class holds commands that a user can use in console '''

    intro = 'Welcome My Love. Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    def do_create(self, arg):
        ''' Creates an instance of the specified class'''
        if len(arg) == 0:
            print("** class name missing ** ")
        elif arg in hbnb_classes:
            n_class = hbnb_classes[arg]()
            print(n_class.id)
            storage.new(n_class)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        ''' Prints all instances based or not on the class name.'''
        all_objs = storage.all()
        if len(arg) == 0:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        else:
            if arg not in hbnb_classes.keys():
                print("** class doesn't exist **")
            else:
                leng = len(arg)
                for key, val in all_objs.items():
                    if key[0:leng] == arg:
                        print(val)

    def do_show(self, arg):
        ''' Shows instance based on the class'''
        class_list = arg.split(" ")
        try:
            key = class_list[0] + "." + class_list[1]
        except:
            pass

        if not arg:
            print("** class name missing ** ")
        else:
            if class_list[0] in hbnb_classes:
                if len(class_list) < 2:
                    print("** instance id missing **")
                elif key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        ''' Deletes instance based on the class'''
        class_list = arg.split(" ")

        try:
            key = class_list[0] + "." + class_list[1]
        except:
            pass

        if not arg:
            print("** class name missing **")
        else:
            if class_list[0] in hbnb_classes:
                if len(class_list) < 2:
                    print("** instance id missing **")
                elif key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        ''' Updates an instance based on the class name '''
        class_list = arg.split(" ")
        leng = len(class_list)

        try:
            key = class_list[0] + "." + class_list[1]
        except:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if class_list[0] in hbnb_classes:
                if leng < 2:
                    print("** instance id missing **")
                elif key not in storage.all().keys():
                    print("** no instance found **")
                elif leng < 3:
                    print("** attribute name missing **")
                elif leng < 4:
                    print("** value missing **")
                else:
                    for cls, instance in storage.all().items():
                        if class_list[1] == instance.id:
                            setattr(instance, class_list[2], class_list[3])
                            storage.save()
            else:
                print("** class doesn't exist **")

    ''' Basic Commands below'''
    def do_quit(self, arg):
        ''' Command exists program: GOOD BYE'''
        print('Thank you for being you')
        return True

    def do_EOF(self, arg):
        ''' Command exists program: See you soon. '''
        print('BYE BUDDY: Do not be a fucker')
        return True

    def Enter(self):
        ''' When there is no input '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
