n = int(input("Enter the number of rows for the hourglass (half height): "))

# Upper part of the hourglass (inverted pyramid)
for i in range(n, 0, -1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line
    print()

# Lower part of the hourglass (pyramid)
for i in range(2, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line
    print()
