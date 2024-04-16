for student in range(0,3,1):
    total = 0
    average = 0
    for subject in range(0,5,1):
        marks = int(input("enter marks: "))
        total = total + marks
    average = total / 5
    print("the average is:", average)
