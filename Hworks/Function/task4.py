def count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')

# output
print(count_vowels("Hello World"))  
# print(count_vowels("Python"))       
