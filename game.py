import cmd 
from room import get_room
import textwrap
import shutil
import tempfile
class Game(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db",self.dbfile)
        
        self.location = get_room(1,self.dbfile)
        self.look()

    def move(self,dir):
        newroom = self.location._neighbor(dir)
        if newroom is None:
            print('You cannot go that way')
        else:
            self.location = get_room(newroom,self.dbfile)
            self.look()

        if newroom == 13:
            exit()

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
    
    def do_save(self,args):
        """Saves a game"""
        shutil.copyfile( self.dbfile,args)
        print('The game was saved to {0}'.format(args))


if __name__ == "__main__":
    g = Game()
    g.cmdloop()