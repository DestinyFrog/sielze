from peewee import *

def get_connection():
    return SqliteDatabase("./db.sqlite3")