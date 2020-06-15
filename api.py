from flask import Flask, Response, request
import requests
import geopy
import json
from geopy.distance import geodesic
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> Main page </h1> <p> To get <a href = http://127.0.0.1:5000/city/London/users>users</a></p>"


@app.route('/city/<city>/users', methods=['GET'])
def get_users(city):
    url = "https://bpdts-test-app.herokuapp.com/"
    max_distance = float(request.args.get('max_distance', default=50))
    mapquest_key = os.environ["MAPQUEST_KEY"] #mapquest key as environmental variable
    geolocator = geopy.MapQuest(mapquest_key)
    location = geolocator.geocode(city) #city from api parameter
    city_coord = (location.latitude, location.longitude) #city coordinates from Map Quest

    #retrieve user data from API
    r_users = requests.get("{}/users".format(url))
    users_data = r_users.json()
    r_city_users = requests.get("{}/city/{}/users".format(url, city))
    city_users = r_city_users.json()
    city_users_data = []
    users = []

    for cities in city_users:
        city_users_data.append(cities)

    #filter results based on distance
    for user in users_data:
        other_location = (user["latitude"], user["longitude"])
        miles_dest = float(geodesic(city_coord, other_location).miles)  # how to calcuate distance between two locations
        if miles_dest <= max_distance:
            users.append(user)

    city_users_dict = {city_user['id']: city_user for city_user in city_users_data}
    all_users = [] + city_users_data

    #removing duplicates
    for user in users:
        if user['id'] in city_users_dict:
            print("removing duplicates")
        else:
            all_users.append(users)

    return Response(json.dumps(all_users))
app.run()