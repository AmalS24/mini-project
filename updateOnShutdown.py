from datetime import datetime
from pymongo import MongoClient
import pymongo

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['LMS']
cur = db.info.find({}).sort('_id',pymongo.DESCENDING).limit(1)
last_person = list(cur).pop(0)
_id = last_person['_id']
now = datetime.now()
exit_t = now.strftime("%I:%M %p") 

db.info.update_one({'_id' : _id},{ '$set' :{'Exit_time': exit_t}})