from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os

from services.way import wayService

load_dotenv()

app = Flask(__name__)

@app.route("/map", methods=["GET"])
def hello_world():
    return render_template('map.html')

#! ____ WAY _____

@app.route("/way")
def get_all():
    data = wayService.get_all()
    return jsonify(data)

@app.route("/way/<uuid:uid>")
def get_one_by_uid(uid):
    data = wayService.get_one_by_uid(uid)
    return jsonify(data)

@app.route("/cway", methods=["POST"])
def create_one_way():
    data = wayService.create_one()
    return jsonify(data)

@app.route("/way/<uuid:uid>/add_point", methods=["POST"])
def add_point_by_id(uid):
    latitude = request.args['latitude']
    longitude = request.args['longitude']
    created_on = request.args['created_on']
    data = wayService.add_point(uid, latitude, longitude, created_on)
    return jsonify(data)

if __name__ == '__main__':
    HOST = os.getenv("HOST") or "localhost"
    PORT = os.getenv("PORT") or 5050
    app.run(HOST, PORT, debug=True)