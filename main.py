# imports json class library
import json

# creates the data dictionary
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests': ['golf','running','videogames'],
    'is_student':False
}

# opens a new json file where it'll store the key and value pairs
with open('data.json', 'w') as json_file:
    json.dump(data,json_file,indent=4)

print("data has been written to data.json")

# 
with open('data.json','r') as json_file:
    loaded_data = json.load(json_file)