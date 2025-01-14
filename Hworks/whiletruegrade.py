while True:
    marks = int(input("Enter the marks (0-100): "))

    #the grade using if-elif-else statements
    if marks < 10 or marks > 100:
        print("Invalid marks entered.")
    elif marks >= 90:
        print("Grade:A")
    elif marks >= 80:
        print("Grade:B")
    elif marks >= 70:
        print("Grade:C")
    elif marks >= 60:
        print("Grade:D")
    elif marks >= 50:
        print("Grade:E")
    else:
        print("Invalid marks entered.")
        break