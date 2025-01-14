string = "Hello World"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")