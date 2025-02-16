from flask import jsonify
import jwt
import os
from uuid import UUID

from util import HttpException
from uuid import uuid4

from db.models import User

class userService:
    def get_full(user:User):
        return {
            "uid": user.uid,
            "name": user.name,
            "email": user.email,
            "password": user.password
        }
        
    def get_user_by_uid(uid:UUID):
        query = User.get( User.uid == uid )
        return userService.get_full(query)

    def login(email:str, password:str):
        try:
            query = User.get(User.email == email)
        except User.DoesNotExist:
            raise HttpException("Usuario não encontrado", 404)

        user = userService.get_full(query)

        if user['password'] != password:
            raise HttpException("Senha Incorreta", 403)
        
        return user
    
    def generate_token(user:User):
        secret = os.getenv("SECRET")
        uid = str(user['uid'])
        token = jwt.encode({"uid": uid}, secret, algorithm="HS256")
        return token

    def create_user(name:str, email:str, password:str):
        uid = uuid4()
        User.create( uid=uid, name=name, email=email, password=password )
