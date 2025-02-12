from models.route import Route

class routeService:
    def get_all() -> list[Route]:
        return Route.select()

    def get_one_by_uid(uid:str) -> Route:
        return Route.select().where( uid=uid )

    def create_one() -> Route :
        route = Route.create()
        return route