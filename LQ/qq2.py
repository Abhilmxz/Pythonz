size = int(input("Enter the size of the square: "))  
for i in range(size):
    for j in range(size):
        if (j == 0 or j == size - 1) and i != size - 1 or (i == size - 1 and j > 0 and j < size - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
