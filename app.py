from flask import Flask, render_template, jsonify, make_response, request, redirect
from dotenv import load_dotenv
import os
import jwt

from util import HttpException
from services.wayService import wayService
from services.userService import userService
from db.models import User
from middlewares.auth import login_required

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def init():
    return render_template('login.html')

@app.route("/signin", methods=["GET"])
def signin():
    return render_template('signin.html')

@app.route("/map", methods=["GET"])
@login_required
def map(current_user):
    return render_template('map.html')

#! _____________ AUTH _____________ !#

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = userService.login(email, password)
    except HttpException as e:
        return render_template('login.html', error_log=str(e) ), e.http_error_code

    token = userService.generate_token(user)

    resp = make_response(jsonify({ "message": "successfully logged" }))
    resp.set_cookie('token', token)
    return resp

@app.route("/signin", methods=["POST"])
def new_user():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    userService.create_user(name, email, password)
    return redirect('/')

@app.route("/logout", methods=["POST"])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('token')
    return resp

#! _____________ WAY ______________ !#

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

#! ___________ ANDROID ____________ !#

@app.route("/android/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = userService.login(email, password)
    except HttpException as e:
        message = {
            "error": str(e)
        }
        return jsonify(message), e.http_error_code

    token = userService.generate_token(user)
    body = {
        "message": "successfully logged",
        "token": token
    }

    return jsonify(body), 200

if __name__ == '__main__':
    HOST = os.getenv("HOST") or "localhost"
    PORT = os.getenv("PORT") or 5050
    MODE = os.getenv("MODE") or "production"

    app.run(HOST, PORT, debug=(MODE == "development") )