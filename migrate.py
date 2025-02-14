from db.models import Point, Way, User, Routine

from db.conn import db

all_tables = [ User, Routine, Way, Point ]

def drop_tables():
    print("Droping all Tables")
    db.drop_tables(all_tables)

def create_tables():
    print("Creating all Tables")
    db.create_tables(all_tables)

drop_tables()
create_tables()

print("Populating Tables")

User.create( uid="b55d5bff-8962-4958-a5e9-522480ec6d26", name="calisto", email="calisto@email.com", password="Framboesa" )