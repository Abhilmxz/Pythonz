# num=int(input("enter a number : "))
# a=0
# b=1
# if num >=1:
#     print(a,end=" ")
# if num >=2:
#     print(b,end=" ")
# for i in range(2,num+1):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c


# amstrong number

num=int(input("Enter A Number: "))
a=len(str(num))
temp=num
revrse=0
b=0
while temp >0:
    b=temp%10
    revrse=revrse+b**a
    temp=temp//10
if num==revrse:
    print("it is an Amstrong number")
else:
    print("its not an amstrong number")