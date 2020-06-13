from flask import Flask, Response
import requests
import geopy
import json
from geopy.distance import geodesic


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> Main page </h1> <p> To get <a href = http://127.0.0.1:5000/user_loc>users</a></p>"


@app.route('/user_loc/', methods=['GET'])
def get_users():
    geolocator = geopy.MapQuest("iBPa7S0BFc8HgAEMwEouQ6J6w4BwmvD2")
    location = geolocator.geocode("London")
    london = (location.latitude, location.longitude)
    r_users = requests.get("https://bpdts-test-app.herokuapp.com/users")
    users_data = r_users.json()
    r_city = requests.get("https://bpdts-test-app.herokuapp.com/city/London/users")
    city_data = r_city.json()
    cities = []
    user = []
    for city in city_data:
        cities.append(city)

    for users in users_data:
        other_location = (users["latitude"], users["longitude"])
        miles_dest = int(geodesic(london, other_location).miles)  # how to calcuate distance between two locations
        if miles_dest <= 50:
            user.append(users)
    city_users_dict = {city_user['id']: city_user for city_user in cities}
    all_users = [] + cities
    for users in user:
        if users['id'] in city_users_dict:
            print("de-duping")
        else:
            all_users.append(users)

    return Response(json.dumps(all_users))
app.run()