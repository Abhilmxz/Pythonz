# print the sum of n natural numbers

n=int(input("Enter a number: "))
# sum1 = 0
# while(n > 0):
#     sum1=sum1+n
#     n=n-1
# print("The sum of first n natural numbers is",sum1)
sum1=0
for i in range(0,n+1):
    sum1=sum1+i
print(f"the sum of first {n} number {sum1}")