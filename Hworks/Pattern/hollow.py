n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        # Print '*' for the border rows and columns, otherwise print space
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
