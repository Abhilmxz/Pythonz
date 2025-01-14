# Define a dictionary
mydict = {"a": 1, "b": 2, "c": 3, "d": 4}

# Input a value from the user
value = input("Enter a value to check: ")
a=0

for i in mydict:
    if mydict[i]==int(value):
        a=1
        break
if a==1:
    print("The value in Dictionary")
else:
    print("The value not in Dictionary")

# Check if the value exists in the dictionary
# if int(value) in mydict.values():
#     print(f"The value`{value}' exists in the dictionary.")
# else:
#     print(f"The value '{value}' does not exist in the dictionary.")


# doubt

# Using for loop
