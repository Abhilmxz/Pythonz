n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(n):
        print("*", end="")
    # Move to the next line
    print()
