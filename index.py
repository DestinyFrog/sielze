from flask import Flask, render_template
from dotenv import load_dotenv
import os

from services.route import routeService

load_dotenv()

app = Flask(__name__)

@app.route("/map", methods=["GET"])
def hello_world():
    return render_template('map.html')

print(routeService.get_all())

'''
@app.route("/routes")
def get_all():
    return routeService.get_all()

@app.route("/create-routes", methods=["GET", "POST"])
def createone_route():
    return routeService.create_one()
    '''

if __name__ == '__main__':
    app.run( os.getenv("HOST") or "localhost", os.getenv("PORT") or 5050)