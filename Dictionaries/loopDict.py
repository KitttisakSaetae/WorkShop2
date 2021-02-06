thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# EX1
for key in thisdict:
    print(key)
# Output :
# brand
# model
# year

# EX2
for key in thisdict:
    print(thisdict[key])
# Output :
# Ford
# Mustang
# 1964

# EX3
for key in thisdict.keys():
    print(key)
# Output :
# brand
# model
# year

# EX4
for value in thisdict.values():
    print(value)
# Output
# Ford
# Mustang
# 1964

# EX5
for key, value in thisdict.items():
    print(key, value)
# Output
# brand Ford
# model Mustang
# year 1964