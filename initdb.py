#!/usr/bin/python2
from __future__ import print_function,division,unicode_literals
import sqlite3
from dbc import dbc
# where to create database.
conn=dbc("storage/data.db")
conn.execute("""CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                username TEXT NOT NULL,
                face_id INTEGER NOT NULL)""" )
conn.execute("""CREATE TABLE photos (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                user INTEGER NOT NULL,
                filename TEXT NOT NULL)""")
