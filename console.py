#!/usr/bin/python3
''' Module contains the entry point of the command interpreter '''
''' REMEMBER TO DELETE MESSAGES '''

import cmd
from models import hbnb_classes, storage

class HBNBCommand(cmd.Cmd):
    ''' Class holds commands that a user can use in console '''

    intro = 'Welcome to HELL. Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    file = None

    def do_create(self, line):
        ''' Creates an instance of the specified class'''
        if len(line) == 0:
            print("** class name missing ** ")
        elif line in hbnb_classes:
            n_class = hbnb_classes[line]()
            print(n_class.id)
            storage.new(n_class)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):


    def do_quit(self, line):
        ''' Command exists program: GOOD BYE'''
        print('Thank you for being you')
        return True

    def do_EOF(self, line):
        ''' Command exists program: See you soon. '''
        print('BYE BUDDY')
        return True

    def Enter(self):
        ''' When there is no input '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
