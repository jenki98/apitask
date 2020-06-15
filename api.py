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

    #retrieve users from API
    r_users = requests.get("{}/users".format(url))
    users_data = r_users.json()
    r_city = requests.get("{}/city/{}/users".format(url, city))
    city_users = r_city.json()
    users = []

    for user in users_data:
        other_location = (user["latitude"], user["longitude"])
        miles_dest = float(geodesic(city_coord, other_location).miles)  # how to calcuate distance between two locations
        if miles_dest <= max_distance:
            users.append(user)
    print(users)
    city_users_dict = {city_user['id']: city_user for city_user in city_users}
    all_users = [] + city_users
    print(all_users)
    for filtered_user in users:
        if filtered_user['id'] in city_users_dict:
            print("de-duping")
        else:
            all_users.append(filtered_user)
    return Response(json.dumps(all_users), mimetype = "application/json")


if __name__ == '__main__':
    app.run()
