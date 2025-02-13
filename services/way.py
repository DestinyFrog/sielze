from playhouse.shortcuts import model_to_dict
from models.way import Way
from models.point import Point
from uuid import uuid4

class wayService:
    def get_all():
        query = Way.select()
        list_way = [model_to_dict(way) for way in query]
        return list_way

    def get_one_by_uid(uid:str):
        query = Way.select().where(Way.uid == uid)
        
        if len(query) < 1:
            return None
        
        return model_to_dict(query[0])

    def create_one():
        id = Way.create( uid = uuid4() )
        [way] = Way.select().where(Way.id == id)
        return model_to_dict(way)

    def add_point(uid, latitude, longitude, created_on):
        id = Point.create( latitude=latitude, longitude=longitude, created_on=created_on )
        [way] = Way.select().where(Way.id == id)
        return model_to_dict(way)