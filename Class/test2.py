# list1=[1,2,"python","program",15.9]
# list2=["amy","bob","charlie","david","emily"]
# print(list1)
# print(list2)


# List indexing

# languages=["python","java","c++"]
# print(languages[0])
# print(languages[1])

# Negative indexing

# languages=["python","java","c++"]
# print(languages[-1])
# print(languages[-3])

# Slicing a Python List

# my_list=['a','b','c','d','e','f','g']
# print(my_list[2:5])
# print(my_list[5:])
# print(my_list[:])

# Add Elements to a Python List

# append()

# numbers=[21,34,54,12]
# print(numbers)
# numbers.append(45)
# print(numbers)

# insert()

# vowel=['a','e','i','u']
# vowel.insert(3,'o')
# print(vowel)

# extend()

# prime_numbers = [2, 3, 5]
# print("List1:", prime_numbers)
# even_numbers = [4, 6, 8]
# print("List2:", even_numbers)
# prime_numbers.extend(even_numbers)
# print("List after append:", prime_numbers) 


#Change List Items

# languages=["python","java","c++"]
# languages[2]='c'
# print(languages)



# Remove Item from a Python List

# pop()

# prime_numbers=[2,3,5,7]
# removed_element=prime_numbers.pop(2)
# print('Removed Element:',removed_element)
# print('Updated List:',prime_numbers)

# Using Del()

# languages=["python","java","c++","c","ruby","R"]
# del languages[1]
# print(languages)
# print(languages[-1])
# print(languages)
# del languages[0:2]
# print(languages)

# Using Remove()

# languages=["python","java","c++","c","ruby","R"]
# languages.remove("c++")
# print(languages)

# Using Reversing a List

# prime_numbers=[2,3,5,7]
# prime_numbers.reverse()
# print("Reversed List:",prime_numbers)

# Python List Operations

# Repetition

# list1=[12,14,16,18,20]
# l=list1*2
# print(l)

# Concatentation

# list1=[12,14,16,18,20]
# list2=[9,10,32,54,86]
# l=list1+list2
# print(l)

# Length

# list1=[12,14,16,18,20]
# a=len(list1)
# print(a)

# Itreation

# list1=[12,14,16,39,40]
# for i in list1:
#     print(i)

# iterating a list

# list=["john","jane","jane","jane","jane"]
# for i in list:
#     print(i)

# Membership

# list=[100,200,300,400,500]
# print(600 in list)
# print(700 in list)

# Python List Built=In Function

# max()

# list1=[103,204,305,406,507]
# print(max(list1))

# min()

# list1=[103,204,305,406,507]
# print(min(list1))


# the intersection of two lists

# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]

# print(list(set(list1).intersection(set(list2))))