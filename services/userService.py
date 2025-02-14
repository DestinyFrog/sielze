from db.models import User

class userService:
    def get_full(user:User):
        return {
            "uid": user.uid,
            "name": user.name,
            "email": user.email,
            "password": user.password
        }
        
    def get_user_by_uid(uid):
        query = User.get( User.uid == uid )
        return userService.get_full(query)
    
    def login(email):
        user = User.get( User.email == email )
        return user