from db.models import User, Routine

class routineService:
	def get_full(routine:Routine):
		return {
			"uid": routine.uid,
			"title": routine.title,
			"description": routine.description,
			"user": routine.user,
			"ways": routine.ways,
			"created_on": routine.created_on,
		}

	def get_routines_by_user(current_user:User):
		query = Routine.get( User == current_user )
		routines = [ routineService.get_full(routine) for routine in query ]
		return routines

	def add_routine(title:str, description:str, user:User):
		routine_id = Routine.create( title=title, description=description, user=user )
		return routine_id

	def append_way(ways:[Way]):
		way_id 