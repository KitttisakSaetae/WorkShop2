import json

# some JSON:
json_string = '{ "name": "Leang", "age": 20, "city": "Rayong"}'

# parse x:
python_dict = json.loads(json_string)

# The result is a Python Dictionary:
print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])