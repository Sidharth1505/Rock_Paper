import json
from config import Files
class Data:
    def fetch_data(self):
        with open(Files.USER_DATA.value, "r") as db:
            file = json.load(db)
            return file

    def append_data(self,file):
        with open(Files.USER_DATA.value, 'w') as db:
            json.dump(file, db, indent = 4,sort_keys =True)

