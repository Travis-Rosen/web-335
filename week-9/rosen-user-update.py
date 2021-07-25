#Travis Rosen
#Rosen-user-service.py
#7/25/2021
#

#Import statements for pprint, datetime, & MongoClient
from pymongo import MongoClient
import pprint
import datetime
#Connecting to the local host 27017 & web335 database
client = MongoClient('localhost', 27017)
db = client.web335

#Updating user document email.
db.users.update_one(
    {"employee_id": "05"},
    {
        "$set":{
            "email":"tmrosen@my365.bellevue.edu"
        }
    }
)
#Printing updated user document with new email through ID.
pprint.pprint(db.users.find_one({"employee_id": "05"}))
#Outputting fields email, firstname, and lastname.
pprint.pprint(db.users.find_one({"first_name": "Frodo"}))
pprint.pprint(db.users.find_one({"last_name": "Baggins"}))
pprint.pprint(db.users.find_one({"email": "tmrosen@my365.bellevue.edu"}))
