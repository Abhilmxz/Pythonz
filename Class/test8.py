# n=int(input("Enter the number of rows: "))
# for i in range(0,n):
#     for j in range(0,n):
#         print(chr(65+j),end=" ")
#     print()

# Alphabet pattern
n=int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,i+1):
        print(chr(65+k),end=" ")
    print()

# 