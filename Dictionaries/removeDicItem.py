# EX1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# Output : {'band': 'Ford', 'year': 1996}

# EX2
thisdic = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)
# Output : {'band': 'Ford', 'model': 'Mustang'}

# EX3
thisdic = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# Output : {'band': 'Ford', 'year': '1964'}

# EX4
thisdic = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)  # Output : ()
