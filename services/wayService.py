from db.models import Way, Point
from uuid import uuid4

class wayService:
    def get_points(point:Point):
        return {
            "id": point.id,
            "latitude": point.latitude,
            "longitude": point.longitude,
            "created_on": point.created_on
        }

    def get_full(way:Way):
        return {
            "uid": way.uid,
            "points": [ wayService.get_points(point) for point in way.points ],
            "created_on": way.created_on
        }

    def get_all():
        query = Way.select()
        list_way = [ wayService.get_full(way) for way in query]
        return list_way

    def get_one_by_uid(uid:str):
        query = Way.get(Way.uid == uid)
        return wayService.get_full(query)

    def create_one():
        id = Way.create( uid = uuid4() )
        way = Way.get(Way.id == id)
        return wayService.get_full(way)

    def add_point(uid, latitude, longitude, created_on):
        way = Way.get( Way.uid == uid )
        id = Point.create( latitude=latitude, longitude=longitude, created_on=created_on, way=way )
        way = Way.get_full(Way.id == id)
        return wayService.get_full(way)