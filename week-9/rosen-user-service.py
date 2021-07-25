#Travis Rosen
#Rosen-user-service.py
#7/22/2021
#Creating Document 

#Import statements for pprint, datetime, & MongoClient
from pymongo import MongoClient
import pprint
import datetime
#Connecting to the local host 27017 & web335 database
client = MongoClient('localhost', 27017)
db = client.web335
#Creating new user information
user = {
    "first_name": "Frodo",
    "last_name": "Baggins",
    "email": "TheShireRules123@me.com",
    "employee_id": "01",
    "date_created": datetime.datetime.utcnow()
}
#Using ID to insert new user
user_id = db.users.insert_one(user).inserted_id
#Using findOne to return results
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "01"}))