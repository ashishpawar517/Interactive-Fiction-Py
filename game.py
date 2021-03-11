import cmd 
from room import get_room
import textwrap

class Game(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.location = get_room(1)
        self.look()

    def move(self,dir):
        newroom = self.location._neighbor(dir)
        if newroom is None:
            print('You cannot go that way')
        else:
            self.location = get_room(newroom)
            self.look()

    def look(self):
        print(self.location.name)
        print('')
        # print(self.location.description)
        for line in textwrap.wrap(self.location.description,72):
            print(line)


    def do_quit(self,args):
        """Quits a game"""
        print('Thank you for playing')
        return True
    
    def do_up(self,args):
        """GO UP"""
        self.move('up')

    def do_down(self,args):
        """GO DOWN"""
        self.move('down')

    def do_n(self,args):
        """ Go North """
        self.move('n')

    def do_s(self,args):
        """ Go South """
        self.move('s')

    def do_e(self,args):
        """ Go East """
        self.move('e')

    def do_w(self,args):
        """ Go West """
        self.move('w')
    

if __name__ == "__main__":
    g = Game()
    g.cmdloop()