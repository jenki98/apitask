import flask
import requests
from geopy import distance

miles_dest = 0.0
london = (51.509865, -0.118092)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])

def home():
    return "<h1> Main page </h1> <p> To get <a href = http://127.0.0.1:5000/user_loc>users</a></p>"

@app.route('/user_loc', methods=['GET'])

def get_users():
    global miles_dest
    r = requests.get("https://bpdts-test-app.herokuapp.com/users")
    data = r.json()

    for items in data:
        first_name = items["first_name"]
        last_name = items["last_name"]
        latitude = items["latitude"]
        longitude = items["longitude"]
        other_location = (latitude, longitude)
        miles_dest = int(distance.distance(london, other_location).miles)  # how to calcuate distance between two locations
        print(latitude, longitude)
        print(miles_dest)
        user_string = first_name + " " + last_name + " - miles from London: " + str(miles_dest) + " miles"
        return user_string
app.run()