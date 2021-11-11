#!/usr/bin/python3
''' Module contains the entry point of the command interpreter '''

import cmd


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to HELL.   Type help or ? to list commands.\n'
    prompt = '(CBRON)'
    file = None

    ''' Basic commands below: 
    @quit and EOF to exit program
    @help: needs to be updated and docummented
    @Enter should not execute with an empty line
    '''
    def do_bye(self):
        'closing HELL, and exit:  BYE'
        print('Thank you for being you')
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None
 
    def do_EOF(self, line):
        ''' Method deals with EOF '''
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
