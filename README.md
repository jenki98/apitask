Users API
===========


Problem Definition (see [here](https://bpdts-test-app.herokuapp.com/instructions))
------------------

> Build an API which calls this API, and returns people who are listed as either living in London, or whose current coordinates are within 50 miles of London. Push the answer to Github, and send us a link


This is an API which calls an API at https://bpdts-test-app.herokuapp.com and filters users returned by that API based on their location. It calls two requests, finding users by City, for example `London` and by co-ordinates that are within 50 miles of London obtaining the London co-ordinates and calculating the distance using Geopy and the MapQuest API. The API removes duplicates based on user Id and returns the list of users to the API interface in JSON format.

Dependencies
------------------

This software requires an API key from Map Quest; you can register for one [here](https://developer.mapquest.com/). Once you have an API key, set the value known as `Consumer Key` in MapQuest as the environment variable `MAPQUEST_KEY`.

This software is written in [Python 3](https://www.python.org/downloads/). You can use Pip to manage the dependencies. To install Pip, download from [here](https://bootstrap.pypa.io/get-pip.py), and then at the command line:

	python get-pip.py


Installation
------------------


	git clone https://github.com/jenki98/apitask.git
	cd apitask
	pip install -r requirements.txt 
	python api.py

The HTTP server runs on port 5000. To query the API for a given city (examples in the dataset being `London`, `Kax`, `Shuanglong`, `Grenada`, `Philipsburg`, etc. - iterating over [all 1000 user IDs](https://bpdts-test-app.herokuapp.com/user/135) can give a full list):

	curl localhost:5000/city/London/users

	[
	  {
	    "id": 135,
	    "first_name": "Mechelle",
	    "last_name": "Boam",
	    "email": "mboam3q@thetimes.co.uk",
	    "ip_address": "113.71.242.187",
	    "latitude": -6.5115909,
	    "longitude": 105.652983
	  },
	  {
	    "id": 396,
	    "first_name": "Terry",
	    "last_name": "Stowgill",
	    "email": "tstowgillaz@webeden.co.uk",
	    "ip_address": "143.190.50.240",
	    "latitude": -6.7098551,
	    "longitude": 111.3479498
	  },
	  {
	    "id": 520,
	    "first_name": "Andrew",
	    "last_name": "Seabrocke",
	    "email": "aseabrockeef@indiegogo.com",
	    "ip_address": "28.146.197.176",
	    "latitude": "27.69417",
	    "longitude": "109.73583"
	  },
	  {
	    "id": 658,
	    "first_name": "Stephen",
	    "last_name": "Mapstone",
	    "email": "smapstonei9@bandcamp.com",
	    "ip_address": "187.79.141.124",
	    "latitude": -8.1844859,
	    "longitude": 113.6680747
	  },
	  {
	    "id": 688,
	    "first_name": "Tiffi",
	    "last_name": "Colbertson",
	    "email": "tcolbertsonj3@vimeo.com",
	    "ip_address": "141.49.93.0",
	    "latitude": 37.13,
	    "longitude": -84.08
	  },
	  {
	    "id": 794,
	    "first_name": "Katee",
	    "last_name": "Gopsall",
	    "email": "kgopsallm1@cam.ac.uk",
	    "ip_address": "203.138.133.164",
	    "latitude": 5.7204203,
	    "longitude": 10.901604
	  },
	  {
	    "id": 266,
	    "first_name": "Ancell",
	    "last_name": "Garnsworthy",
	    "email": "agarnsworthy7d@seattletimes.com",
	    "ip_address": "67.4.69.137",
	    "latitude": 51.6553959,
	    "longitude": 0.0572553
	  },
	  {
	    "id": 322,
	    "first_name": "Hugo",
	    "last_name": "Lynd",
	    "email": "hlynd8x@merriam-webster.com",
	    "ip_address": "109.0.153.166",
	    "latitude": 51.6710832,
	    "longitude": 0.8078532
	  },
	  {
	    "id": 554,
	    "first_name": "Phyllys",
	    "last_name": "Hebbs",
	    "email": "phebbsfd@umn.edu",
	    "ip_address": "100.89.186.13",
	    "latitude": 51.5489435,
	    "longitude": 0.3860497
	  }
	]

By default, the maximum distance from the target city that marks a person as "in" that city is 50 miles, but this is configurable via the `max_distance` query string parameter:

	curl localhost:5000/city/Kax/users?max_distance=200

	[
	  {
	    "id": 1,
	    "first_name": "Maurise",
	    "last_name": "Shieldon",
	    "email": "mshieldon0@squidoo.com",
	    "ip_address": "192.57.232.111",
	    "latitude": 34.003135,
	    "longitude": -117.7228641
	  },
	  {
	    "id": 854,
	    "first_name": "Nelly",
	    "last_name": "Thurley",
	    "email": "nthurleynp@joomla.org",
	    "ip_address": "46.72.120.66",
	    "latitude": 34.003135,
	    "longitude": -117.7228641
	  },
	  {
	    "id": 166,
	    "first_name": "Tera",
	    "last_name": "Bradnum",
	    "email": "tbradnum4l@people.com.cn",
	    "ip_address": "29.148.71.42",
	    "latitude": 35.1083109,
	    "longitude": 136.1458137
	  },
	  {
	    "id": 264,
	    "first_name": "Lawry",
	    "last_name": "Bertomier",
	    "email": "lbertomier7b@paginegialle.it",
	    "ip_address": "255.119.168.3",
	    "latitude": 34.6494619,
	    "longitude": 135.7837972
	  },
	  {
	    "id": 725,
	    "first_name": "Gisella",
	    "last_name": "Kanwell",
	    "email": "gkanwellk4@imgur.com",
	    "ip_address": "71.159.92.84",
	    "latitude": 35.5205328,
	    "longitude": 135.7708561
	  },
	  {
	    "id": 903,
	    "first_name": "Dave",
	    "last_name": "Galero",
	    "email": "dgalerop2@topsy.com",
	    "ip_address": "231.186.88.149",
	    "latitude": 33.426956,
	    "longitude": 130.6436108
	  }
	]

