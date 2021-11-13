#!/usr/bin/python3
''' Module contains the entry point of the command interpreter '''
import cmd
from types import new_class
from models import hbnb_classes, storage


class HBNBCommand(cmd.Cmd):
    '''Class holds commands that a user can use in console'''

    intro = 'Welcome to HBNB. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def default(self, arg):
        '''Runs class commands: <class name>.command()'''
        arg_list = arg.split('.')
        if len(arg_list) == 2:
            if arg_list[0] in hbnb_classes:
                if arg_list[1] == "all()":
                    self.do_all(arg_list[0])
                elif arg_list[1] == "count()":
                    self.do_count(arg_list[0])

    def do_count(self, arg):
        '''Counts number of instances of a class'''
        all_objs = storage.all()
        count = 0
        if arg not in hbnb_classes:
            print("** class doesn't exist **")
        else:
            for key in all_objs.keys():
                if arg in key:
                    count += 1
            print(count)

    def do_create(self, arg):
        '''Creates an instance of the specified class\n'''
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
        '''Prints all instances based or not on the class name.\n'''
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
        '''Shows instance based on the class\n'''
        class_list = arg.split(" ")
        try:
            key = class_list[0] + "." + class_list[1]
        except Exception:
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
        '''Deletes instance based on the class\n'''
        class_list = arg.split(" ")

        try:
            key = class_list[0] + "." + class_list[1]
        except Exception:
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
        '''Updates an instance based on the class name\n'''
        cls_li = arg.split(" ")
        leng = len(cls_li)

        try:
            key = cls_li[0] + "." + cls_li[1]
        except Exception:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if cls_li[0] in hbnb_classes:
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
                        if cls_li[1] == instance.id:
                            setattr(instance, cls_li[2], cls_li[3].strip('"'))
                            storage.save()
            else:
                print("** class doesn't exist **")

    ''' Basic Commands below'''
    def do_quit(self, arg):
        '''QUIT command exists program\n'''
        return True

    def do_EOF(self, arg):
        '''EOF Command exists program\n'''
        return True

    def emptyline(self):
        '''When there is no input '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
