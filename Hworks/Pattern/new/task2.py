for i in range(6):
    for j in range(5):
        if (i == 0 or i == 5) and j in [1, 2, 3]:
            print("*", end=" ")
        elif (i == 1 or i == 4) and j in [0, 4]:
            print("*", end=" ")
        elif (i == 2 or i == 3) and j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()