import datetime
from peewee import *

from db.conn import db

class BaseModel(Model):
    class Meta:
        database = db

class Way(BaseModel):
    id = IntegerField(primary_key=True)
    uid = UUIDField(unique=True)

    created_on = DateTimeField(default=datetime.datetime.now)

class Point(BaseModel):
    id = IntegerField(primary_key=True)
    latitude = DoubleField()
    longitude = DoubleField()

    way = ForeignKeyField(Way, related_name="points")

    created_on = DateTimeField(default=datetime.datetime.now)