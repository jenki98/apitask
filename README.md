This is an API which calls an API at  https://bpdts-test-app.herokuapp.com and filters users based on their location. It calls two requests, finding users by City ‘London’ and by co-ordinates that are within 50 miles of London obtaining the London co-ordinates and calculating the distance using Geopy and the MapQuest API. The API removes duplicates based on user Id and returns the list of users to the API interface in JSON format.
Installation:
This software requires an API key from Map Quest which can be found here: https://www.mapquest.co.uk/ 
The API key is used as an environment variable MAPQUEST_KEY.
This software is written in Python 3 which can be installed from: https://www.python.org/downloads/
To install pip download https://bootstrap.pypa.io/get-pip.py and from command line use the command:
python get-pip.py

To run software in command line:

git clone https://github.com/jenki98/apitask.git
cd apitask
pip install -r requirements.txt 
