def Subtract(num1,num2):
    if (num1 >= num2):
        return num1 - num2
    else:
        return num2 - num1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum of 2 numbers =", Subtract(num1,num2))