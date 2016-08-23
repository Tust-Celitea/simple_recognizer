#!/usr/bin/python2
from __future__ import print_function,division,unicode_literals
import sqlite3
class dbc(object):
    '''define a pre-configured database connection.'''
    def __init__(self,target):
        self.connection=sqlite3.connect(target)
        self.cursor=self.connection.cursor()
        self.execute=self.cursor.execute
        self.commit=self.connection.commit
        self.close=self.connection.close

if __name__=="__main__":
    conn=dbc("demo.db")
    try:
        conn.execute("""CREATE TABLE demobase (
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        data TEXT NOT NULL,
                        value INTEGER NOT NULL)""")
    except sqlite3.OperationalError:
        pass
    for i in range(5):
        conn.execute("INSERT INTO demobase (data,value) VALUES (?, ?)",(i,i**i))
    conn.execute("SELECT data,value FROM demobase")
    for i in conn.cursor.fetchall():
        print(i)
    conn.commit()
    conn.close()
