# num = 1234
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10

# print("Reversed Number: " + str(reversed_num))

num =int(input("Enter a Number : "))
x=num
a=str(num)[::-1]
if str(x)==a:
    print("paliandrome")
else:
    print("Not paliandrome")