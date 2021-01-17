# Example1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # Output : ["apple", "cherry"]

# Example2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Output : ["apple", "cherry"]

# Example3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # Output : ["apple", "banana"]

# Example4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # Output : ["banana", "cherry"]

# Example5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # Output : []
