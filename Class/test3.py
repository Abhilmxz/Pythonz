#Sets

# a=set()
# print(type(a))

# Using sets

# set1={1,6,4,'abc'}
# print(type(set1))

# Using Set methods
# days=set(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# print(days)
# print(type(days))
# for i in days:
#     print(i)

# Using Add methods
# months=set(['january','february','march','april','may','june'])
# print(months)
# months.add('july')
# print(months)

# using Update method

# months=set(['january','february','march','april','may','june'])
# print(months)
# months.update(['july','august'])
# print(months)   

# Removing items From The set

# Using Discard method
# month=set(["january","february","march"])
# print(month)
# month.discard("march")
# print(month)

# Using Remove method

# month=set(["january","february","march"])
# print(month)
# month.remove("january")
# print(month)

# Python set operations
# Union of 2 sets

# day1={"monday","tuesday","wednesday","thursday"}
# day2={"friday","saturday","sunday"}
# print(day1|day2)

# Intersection of 2 sets

# day1={"monday","tuesday","wednesday","thursday"}
# day2={"monday","tuesday","sunday","friday"}
# print(day1&day2)

# Set Comparison

# day1={"monday","tuesday","wednesday","thursday"}
# day2={"monday","tuesday"}
# day3={"monday","tuesday","friday"}
# # print(day1>day2)
# # print(day1<day2)
# print(day1==day3)

# Creating Tuples

# tuple_data=(0,1,2,3,2,3,1,2)
# print(tuple_data)

# Empty_tuple=()

# my_tuple=()
# print(my_tuple)

# Nested tuple

# my_tuple=("mouse",[8,4,6],(1,2,3))
# print(my_tuple)

# Access Elements
# Indexing

# letters=("p","r","o","g","r","a","m","i","z")
# print(letters[0])
# print(letters[5])

# Negative Indexing

# letters=("p","r","o","g","r","a","m","i","z")
# print(letters[-1])
# print(letters[-3])

# Slicing in tuples

# my_tuple=("p","r","o","g","r","a","m","i","z")
# print(my_tuple[1:4])
# print(my_tuple[:-7])
# print(my_tuple[7:]) 
# print(my_tuple[:])

# Tuple repetition
# tuple_=('python',"tuple")
# print("Orginal tuple is:",tuple_)

# tuple_=('python',"tuple")
# print("new tuple is:",tuple_*3)

# Tuple methods
# my_tuple=("a","p","p","l","e")
# print(my_tuple.count("p"))
# print(my_tuple.index("l"))

# Iterating through Tuples    

# laguages=("python","java","c","c++")
# for languages in laguages:
#     print(languages)

# Check if an item Exits in tuple

# languages=("python","java","c","c++")
# print("java" in languages)
# print("ruby" in languages)

# Create a Dictionary

# capital_city={"India":"Delhi","USA":"Washington DC","UK":"London"}
# print(capital_city)

# Add Elements to a python Dictionary

# capital_city={"India":"Delhi","USA":"Washington DC","UK":"London"}
# print("Initial dictionary:",capital_city)
# capital_city["France"]="Paris"
# print("Updated dictionary:",capital_city)

# Change Value Of Dictionary

# student_id={"student1":101,"student2":102,"student3":103}
# print("Intial Dictionary:",student_id)
# student_id["student3"]=104
# print("Updated Dictionary:",student_id)

# Access Elements in Dictionary

# student_id={"student1":101,"student2":102,"student3":103}
# print(student_id["student1"])
# print(student_id["student3"])

# Removing Elements From Dictionary

# student_id={"student1":101,"student2":102,"student3":103}
# print("Intial Dictionary:",student_id)
# del student_id["student1"]
# print("Updated Dictionary:",student_id)

#Iterating Through Dictionary

# square={1:1,3:9,5:25,7:49,9:81}
# for i in square:
#     print(square[i])

# Copy A Dictionary
# thisdict ={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
#     }
# mydict=thisdict.copy()
# print(mydict)

#Using zip for creating Dictionary

key=[1,2,3,4,5]
values=["one","two","three","four","five"]
dictionary= dict(zip(key,values))
print(dictionary)