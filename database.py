import json
import os

class Database:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump({}, file)

    def write(self, key, value):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        data[key] = value
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        return
        
    def read(self, key):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        
        return data[key]
    

if __name__ == "__main__":
    db = Database("data.json")
    db.write("test", "hello")
    db.write("test2", "world")
    db.write("test3", {"hello": "world"})
    print(db.read("test"))
    print(db.read("test3"))