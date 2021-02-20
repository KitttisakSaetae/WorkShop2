import json

# a Python object (dict):
python_dict = {"name": "Leang", "age": 20, "city": "Rayong"}

# Convert into JSON:
json_string = json.dumps(python_dict)

# the result is a JSON string:
print(json_string)