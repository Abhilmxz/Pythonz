# for i in range(0,5):
#     for j in range (0,5):
#         print("*",end= " ")
#     print()

# down pattern

# n=5

# for i in range (0,n):
#     for j in range (0,n-i):
#         print("*",end=" ")
#     print()

# up pattern
# n=5
# for i in range (0,n):
#     for j in range (0,i+1):
#         print("*",end=" ")
#     print()

#Triangle pattern

# n=int(input("Enter the number of rows: "))
# for i in range (0,n):
#     for j in range (0,n-i):
#         print(" ",end=" ")
#     for k in range (0,i+1):
#         print("*",end=" ")
#     print()



# while True:
#     print("enter your choice 1.add 2.sub 3.mul 4.div 5.exit")
#     choice=int(input("Enter the Number : "))
#     if choice ==1:
#         a=int(input("Enter your first number: "))
#         b=int(input("Enter your second number: "))
#         c=a+b
#         print(c)
#     elif choice ==2:
#         a=int(input("Enter your first number: "))
#         b=int(input("Enter your second number: "))
#         c=a-b
#         print(c)
#     elif choice ==3:
#         a=int(input("Enter your first number: "))
#         b=int(input("Enter your second number: "))
#         c=a*b
#         print(c)
#     elif choice ==4:
#         a=int(input("Enter your first number: "))
#         b=int(input("Enter your first number: "))
#         if b !=0:
#             c=a/b
#             print(c)
#         else:
#             print("entered value is not valid")
#     elif choice==5:
#         break


rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()