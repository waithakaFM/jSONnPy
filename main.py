# JSON: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on
# JavaScript object syntax
# for more info: https://www.python-engineer.com/courses/advancedpython/11-json/


# encoding/ serialization - from dict to json format
import json


person = {'fname': 'Mwangi', 'lname':'Waithaka', 'age':21, 'city':'Nairobi', 'married':False,
          'titles': ['programmer', 'project manager', 'computer scientist']}

personJSON = json.dumps(person, indent=4, sort_keys=True)
# print(personJSON)

# open it with file
with open('person.json', 'w') as file:  # create a file named person.json
    json.dump(person, file, indent=4)


# decoding/ deserialization - from json to python file
personDict = json.loads(personJSON)


# from json file to .py
with open('person.json', 'r') as file:
    personDict = json.load(file)
    print(personDict)
