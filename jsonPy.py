import json


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Waithaka', 21)

# userJSON = json.dumps(user)  # get TypeError: Object of type User is not JSON serializable


# write custom encoding function

# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#     else:
#         raise TypeError('Object of type User is not JSON serializable')
#
#
# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)

# another way to implement custom json encoder

from json import JSONEncoder


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}

        return JSONEncoder.default(self, o)


# userJSON = json.dumps(user, cls=UserEncoder)
# # or
userJSON = UserEncoder().encode(user)
print(userJSON)

# decode our object back
user = json.loads(userJSON)
print(type(user))
print(user)  # is now a dict but not object yet


# decode it into an object
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)  # now user is an object
print(user.age)
