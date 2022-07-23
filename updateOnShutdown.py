from datetime import datetime
from pymongo import MongoClient
import bson.objectid as ob

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['LMS']
f = open("C:\\Users\\Amal\\Desktop\\id.txt","r")
_id = ob.ObjectId(f.read())
f.close()
now = datetime.now()
exit_t = now.strftime("%I:%M %p") 
db.info.update_one({'_id' : _id},{ '$set' :{'Exit_time': exit_t}})