import datetime
from peewee import *
from models.way import Way

from db.conn import db

class Point(Model):
    id = IntegerField(primary_key=True)
    latitude = DoubleField()
    longitude = DoubleField()
    route = ForeignKeyField(Way, backref="points")
    created_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
