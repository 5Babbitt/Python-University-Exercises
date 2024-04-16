counter = 1
empNum = int(input("Enter number of employees: "))

while counter <= empNum:
    salary = int(input("Enter Salary(-1 to end): "))
    
    if ((salary >= 0) and (salary < 3000)):
        tax = 0
    elif ((salary >= 3000) and (salary < 5000)):
        tax = 6
    elif ((salary >= 5000) and (salary < 7000)):
        tax = 8
    elif ((salary >= 7000) and (salary < 8000)):
        tax = 12
    elif ((salary >= 8000) and (salary < 9000)):
        tax = 16
    elif (salary <= -1):
        break
    else:
        tax = 40
    
    actualSalary = salary - (salary * tax/100)
    print("Actual Salary:", actualSalary)

    counter = counter + 1
       




