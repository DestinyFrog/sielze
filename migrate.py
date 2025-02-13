from models.point import Point
from models.way import Way
from models.routine import Routine

from db.conn import db

all_tables = [ Way, Point, Routine ]

def drop_tables():
    print("Droping all Tables")
    db.drop_tables(all_tables)

def create_tables():
    print("Creating all Tables")
    db.create_tables(all_tables)

drop_tables()
create_tables()