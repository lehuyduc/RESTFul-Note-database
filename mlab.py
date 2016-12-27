#mongodb://<dbuser>:<dbpassword>@ds145128.mlab.com:45128/techkids_note
import mongoengine

host = "ds145128.mlab.com"
port = 45128
db_name = "techkids_note"
user_name = "admin"
password = "lalalala1212"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
   import json
   return [json.loads(item.to_json()) for item in l]

def item2json(item):
   import json
   return json.loads(item.to_json());


