#!/usr/bin/python3
''' Module contains the entry point of the command interpreter '''

import cmd
#from models import storage


class HBNBCommand(cmd.Cmd):
    ''' Class holds commands that a user can use in console '''

    intro = 'Welcome to HELL. Type help or ? to list commands.\n'
    prompt = '(CBRON) '
    file = None

    ''' ¡¡¡¡ in the works !!!!
    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing ** ")
        else:
            storage.new(line)
            storage.save() '''

    def do_quit(self, line):
        ''' Command exists program: GOOD BYE'''
        print('Thank you for being you')
        return True

    def do_EOF(self, line):
        ''' Command exists program: See you soon. '''
        print('BYE BUDDY')
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
