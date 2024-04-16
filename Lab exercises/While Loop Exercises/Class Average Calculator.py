name = input("Enter name[blank to end]: ")
score = int(input("Enter student's exam score[999 to end]: "))

classAvg = 0
num = 0
classTotal = 0

while (score != 999):
    if(score > 100) or (score < 0):
        print("Invalid Entry!")
        num -= 1
        score = 0
    classTotal += score
    num += 1
    name = input("Enter name[blank to end]: ")
    score = int(input("Enter student's exam score[999 to end]: "))
    
classAvg = classTotal / num
print("\nClass average: %.2f" % classAvg)