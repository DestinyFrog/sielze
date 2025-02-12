import datetime
from peewee import *
from models.route import Route

from db.conn import get_connection

class Point(Model):
    id = IntegerField(primary_key=True)
    latitude = DoubleField()
    longitude = DoubleField()
    route = ForeignKeyField(Route, backref="points")
    created_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = get_connection()
