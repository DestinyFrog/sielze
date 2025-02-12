import datetime
from peewee import *

from db.conn import get_connection

class Route(Model):
    id = IntegerField(primary_key=True)
    uid = UUIDField(unique=True)

    created_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = get_connection()
