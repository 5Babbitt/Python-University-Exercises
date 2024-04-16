for student in range(0,3,1):
    total = 0
    average = 0
    subject = int(input("Enter number of subjects: "))
    for subject in range(0,subject,1):
        marks = int(input("enter marks: "))
        total = total + marks
    average = total / (subject + 1)
    print("the average is:", average)