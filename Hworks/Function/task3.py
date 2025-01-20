def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))

# output:
print(sum_of_digits(1234))  # Output: 10
