import flask
import requests
from geopy import distance

miles_dest = 0.0
london = (51.509865, -0.118092)

app = flask.Flask(__name__)
app.config["DEBUG"] = True
def get_data():
    x = 2

@app.route('/', methods=['GET'])
def home():
    return "<h1> Main page </h1> <p> To get <a href = http://127.0.0.1:5000/user_loc>users</a></p>"


@app.route('/user_loc', methods=['GET'])
def get_users():
    global miles_dest
    r = requests.get("https://bpdts-test-app.herokuapp.com/users")
    data = r.json()
    users = {}
    count = 1
    for items in data:
       #first_name = items["first_name"]
      # last_name = items["last_name"]
        user_id = items["id"]
        latitude = items["latitude"]
        longitude = items["longitude"]
        other_location = (latitude, longitude)
        miles_dest = int(distance.distance(london, other_location).miles)  # how to calcuate distance between two locations
        if miles_dest <= 50:
            user_string = str(items) +  str(miles_dest) + " miles " + str(user_id)
            print(items)
            users[count] = user_string
        count += 1
    return users

app.run()