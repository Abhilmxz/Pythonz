while True:
    print("enter your choice 1.add 2.sub 3.mul 4.div 5.exit")
    choice=int(input("Enter the Number : "))
    if choice ==1:
        a=int(input("Enter your first number: "))
        b=int(input("Enter your second number: "))
        c=a+b
        print(c)
    elif choice ==2:
        a=int(input("Enter your first number: "))
        b=int(input("Enter your second number: "))
        c=a-b
        print(c)
    elif choice ==3:
        a=int(input("Enter your first number: "))
        b=int(input("Enter your second number: "))
        c=a*b
        print(c)
    elif choice ==4:
        a=int(input("Enter your first number: "))
        b=int(input("Enter your first number: "))
        if b !=0:
            c=a/b
            print(c)
        else:
            print("entered value is not valid")
    elif choice==5:
        break