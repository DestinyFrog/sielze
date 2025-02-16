import datetime
from peewee import *

from db.conn import db

class BaseModel(Model):
    class Meta:
        database = db
        
class User(BaseModel):
    id = IntegerField(primary_key=True)
    uid = UUIDField(unique=True)
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

class Routine(BaseModel):
    id = IntegerField(primary_key=True)
    uid = UUIDField(unique=True)
    title = CharField()
    description = TextField()
    public = BooleanField(default=False)
    user = ForeignKeyField(User, related_name="routines", null=True)

class Way(BaseModel):
    id = IntegerField(primary_key=True)
    uid = UUIDField(unique=True)
    
    routine = ForeignKeyField(Routine, related_name="ways", null=True)

    created_on = DateTimeField(default=datetime.datetime.now)

class Point(BaseModel):
    id = IntegerField(primary_key=True)
    latitude = DoubleField()
    longitude = DoubleField()

    way = ForeignKeyField(Way, related_name="points")

    created_on = DateTimeField(default=datetime.datetime.now)