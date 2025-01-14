n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line
    print()
