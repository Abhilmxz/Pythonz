# def is_armstrong(n):
#     num_str = str(n)  # Converting the number to a string here
#     num_digits = len(num_str)  # Geting the number of digits in the number
#     return sum(int(digit) ** num_digits for digit in num_str) == n

# # output amstrong
# print(is_armstrong(153))  # Output: True
# print(is_armstrong(9474)) # Output: True
# print(is_armstrong(123))  # Output: False



def is_armstrong(n):
    num_str = str(n)
    return sum(int(digit) ** len(num_str) for digit in num_str) == n


print(is_armstrong(153))  
print(is_armstrong(123))
