from db.models import Point, Way

from db.conn import db

all_tables = [ Way, Point ]

def drop_tables():
    print("Droping all Tables")
    db.drop_tables(all_tables)

def create_tables():
    print("Creating all Tables")
    db.create_tables(all_tables)

drop_tables()
create_tables()

way = Way.create( uid = "b34b5ec8-2d7d-4084-93c5-d2bbd13016d0" )
Point.create( latitude=-23.454163, longitude=-46.534096, way=way )
Point.create( latitude=-23.5489, longitude= -46.6388, way=way )

print("Populating Tables")