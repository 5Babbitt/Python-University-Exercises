import time
choice = input("For first 20 numbers, enter 1, \nFor first 20 even numbers, enter 2, \nFor the times table, enter 3, \nEntry: ")

while(choice == "1") or (choice == "2") or (choice == "3"):
    if(choice == "1"):
        x = int(0)

        for i in range(20):
            x += 1
            print(x)
            time.sleep(0.1)

    if(choice == "2"):
        x = int(0)

        for i in range(20):
            x += 2
            print(x)
            time.sleep(0.1)

    if(choice == "3"):
        num = 0
        prod = 0
        multiple = int(input("Enter number to be multiplied: "))

        for i in range(13):
            
            prod = multiple * num
            print(multiple, "x", num, "=", prod)
            num += 1
            time.sleep(0.1)
    
    choice = input("\nFor first 20 numbers, enter 1, \nFor first 20 even numbers, enter 2, \nFor the times table, enter 3, \nEntry: ")