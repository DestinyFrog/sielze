from flask import request, jsonify
from functools import wraps
import jwt
import os

from services.userService import userService

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({"message": "token is missing"}), 401
        
        secret = os.getenv("SECRET")
        
        try:
            data = jwt.decode(token, secret, algorithms=["HS256"])
            uid = data['uid']
            current_user = userService.get_user_by_uid(uid)
            return f(current_user, *args, **kwargs)
        except:
            return jsonify({"message": "token is invalid or expired"}), 401
    return decorated