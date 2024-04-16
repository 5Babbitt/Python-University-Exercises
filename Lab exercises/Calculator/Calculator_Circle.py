import math

def Diameter(radius):
    return radius * 2

def Area(radius):
    return math.pi * radius ** 2

def Circumference(radius):
    return 2 * math.pi * radius

def Menu():
    print ("Circle Calculator\n-----------------\n\n\t1. Diameter\n\t2. Circumference\n\t3. Area")

    choice = int(input("\nChoose the calculation from the given options: "))
    r = float(input("Input radius: "))
    
    if (choice == 1):
        print("Diameter = %.4f" % Diameter(r))
    elif (choice == 2):
        print("Circumference = %.4f" % Circumference(r))
    elif (choice == 3):
        print("Area = %.4f" % Area(r))
    else:
        print("Invalid Entry")

Menu()
        