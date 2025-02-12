from models.point import Point
from models.point import Route

from db.conn import get_connection

all_tables = [ Route, Point ]

def drop_tables():
    print("Droping all Tables")
    get_connection().drop_tables(all_tables)

def create_tables():
    print("Creating all Tables")
    get_connection().create_tables(all_tables)

drop_tables()
create_tables()