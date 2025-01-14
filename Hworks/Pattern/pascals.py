# Python program for Pascal's Triangle using Binomial
# Coefficient in O(n^3) and O(1) Space 

def binomialCoeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

# Function to print first n rows 
# of Pascal's Triangle 
def printPascal(n):
    mat = []
    
    # Iterate through every row and
    # print entries in it
    for row in range(n):
        arr = []
        for i in range(row + 1):
            arr.append(binomialCoeff(row, i))
        mat.append(arr)
    return mat

n = int(input("Enter your row: "))
mat = printPascal(n)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print()