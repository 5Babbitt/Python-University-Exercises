choice = str(input("Would you like to start(y/n): "))
newNum = int(input("Enter new number(-1 to end): "))
highNum = 0

while (newNum != -1):
    newNum = int(input("Enter new number(-1 to end): "))
    if (newNum > highNum):
        highNum = newNum
print("The largest number is:", highNum)
    
