n=int(input("Enter the number of row : "))

for i in range (n,0,-1):
    for j in range (n-i):
        print(" ",end="")
    for j in range (2*i-1):
        if i==0 or i==n or j==2*i-2 or j==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()