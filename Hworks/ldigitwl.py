number = int(input("Enter a number: "))
largest = 0

while number > 0:
    largest = max(largest, number % 10)
    number //= 10

print("The largest digit is:", largest)