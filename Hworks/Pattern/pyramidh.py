n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print the stars and spaces
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    # Move to the next line
    print()
