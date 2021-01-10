x = "Awesome"


def myFunc():
    global x
    # print (x = Awesome)
    print("Python is " + x)
    x = "Fantastic"


myFunc()
# print (x = Fantastic)
print("Python is " + x)