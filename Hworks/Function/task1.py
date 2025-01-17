def is_palindrome(s):
    return s == s[::-1]

# printing palindrome:
print(is_palindrome("level"))  # True
print(is_palindrome("radar"))  # False
