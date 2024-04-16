mark = int(input("Enter your marks[Enter 999 to end]: "))
grade = ["A", "B", "C", "D", "F","Invalid Entry!"]

while(mark != 999):
    if (mark > 100 or mark < 0):
        print(grade[5])
    elif (mark <= 49):
        print("Your Grade is:", grade[4])
    elif (mark <= 59):
        print("Your Grade is:", grade[3])
    elif (mark <= 69):
        print("Your Grade is:", grade[2])
    elif (mark <= 79):
        print("Your Grade is:", grade[1])   
    else:
        print("Your Grade is:", grade[0])

    mark = int(input("\nEnter your marks[Enter 999 to end]: "))

