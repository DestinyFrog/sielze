import datetime
from peewee import *

from db.conn import db

class Way(Model):
    id = IntegerField(primary_key=True)
    uid = UUIDField(unique=True)
    created_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db