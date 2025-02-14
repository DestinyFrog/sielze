from flask import Flask, render_template, jsonify, make_response, request, redirect
from dotenv import load_dotenv
import os
import jwt

from services.wayService import wayService
from services.userService import userService
from db.models import User
from middlewares.auth import login_required

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def init():
    return render_template('login.html')

@app.route("/map", methods=["GET"])
@login_required
def map(current_user):
    return render_template('map.html')

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    
    try:
        query = User.get(User.email == email)
    except User.DoesNotExist :
        return jsonify({'message': "user not found"}), 404
    
    user = userService.get_full(query)
        
    if user['password'] != password:
        return jsonify({'message': "password is incorrect"}), 403

    secret = os.getenv("SECRET")
    uid = str(user['uid'])
    token = jwt.encode({"uid": uid}, secret, algorithm="HS256")

    resp = make_response(redirect('/map'))
    resp.set_cookie('token', token)
    return resp

@app.route("/way")
@login_required
def get_all(current_user):
    data = wayService.get_all()
    return jsonify(data)

@app.route("/way/<uuid:uid>")
def get_one_by_uid(uid):
    data = wayService.get_one_by_uid(uid)
    return jsonify(data)

@app.route("/way", methods=["POST"])
def create_one_way():
    body = request.get_json()
    points = body['points']
    data = wayService.create_one(points)
    return jsonify(data)

if __name__ == '__main__':
    HOST = os.getenv("HOST") or "localhost"
    PORT = os.getenv("PORT") or 5050
    MODE = os.getenv("MODE") or "production"

    app.run(HOST, PORT, debug=(MODE == "development") )