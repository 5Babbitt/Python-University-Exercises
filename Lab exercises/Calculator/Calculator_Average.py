def AverageOf3(num1,num2,num3):
    total = num1 + num2 + num3
    return total/3

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print("The average of these 3 numbers is: ", AverageOf3(num1,num2,num3))