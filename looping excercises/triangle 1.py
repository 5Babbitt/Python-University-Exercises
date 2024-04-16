rowNum = int(input("Enter number of rows from 1 to 9: "))

if(rowNum < 1 or rowNum > 9):
    print("Invalid Output")
else:
    for i in range(rowNum, 0, -1):
        if(i % 2 == 0):
            printString = "*"
        else:
            printString = "@"
        print("")
        for x in range(0, i, 1):
            print(printString, sep= "",end= "")
            
    
