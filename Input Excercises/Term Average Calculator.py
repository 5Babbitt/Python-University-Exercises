choice = str(input("Would you like to start(y/n)"))

while (choice == "y"):
    total = 0
    average = 0
    subject = int(input("Enter number of subjects: "))
    for subject in range(0,subject,1):
        marks = int(input("enter marks: "))
        total = total + marks
    average = total / (subject + 1)
    print("the average is:", average)
    choice = str(input("would you like to continue(y/n)"))