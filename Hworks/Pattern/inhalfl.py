rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    # Print spaces to align the stars to the right
    for space in range(rows - i):
        print(" ", end=" ")
    # Print stars
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
