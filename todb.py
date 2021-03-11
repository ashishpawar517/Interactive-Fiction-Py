import sys
import sqlite3
import os
import os.path

def main(dbname):
    con = sqlite3.connect(dbname)
    con.execute('create table if not exists rooms(id integer primary key,json text not null)')
    con.commit()

    for filename in os.listdir():
        base,extension = os.path.splitext(filename)
        if extension == '.json':
            with open(filename,'r') as f:
                json = f.read()
                print("Inserting room {0}".format(int(base)))
                con.execute('insert into rooms(id,json) values(?,?);',(int(base),json))
                con.commit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: {0} <database name>'.format(sys.argv[0]))
    else:
        main(sys.argv[1])