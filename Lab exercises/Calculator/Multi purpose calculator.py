
def Add(num1,num2):
    return num1 + num2

def Subtract(num1,num2):
    return num1 - num2

def Multiply(num1,num2):
    return num1 * num2

def Divide(num1,num2):
    return num1 / num2

print("Calculator Program \n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n")

choice = int(input("Choose the operation from the given options: "))
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

if(choice == 1):
    print(num1, " + ", num2, " = ", Add(num1,num2))
elif(choice == 2):
    print(num1, " - ", num2, " = ", Subtract(num1,num2))
elif(choice == 3):
    print(num1, " x ", num2, " = ", Multiply(num1,num2))
elif(choice == 4):
    print(num1, " ÷ ", num2, " = ", Divide(num1,num2))
else:
    print("Invalid Input")