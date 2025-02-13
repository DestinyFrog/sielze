import datetime
from peewee import *

from db.conn import db

class Routine(Model):
    id = IntegerField(primary_key=True)
    title = CharField()
    description = TextField()

    created_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
