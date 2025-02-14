from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os

from services.wayService import wayService

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return render_template('map.html')

@app.route("/way")
def get_all():
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