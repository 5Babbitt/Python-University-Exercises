import os

os.system("cls")

COLOURS = {\
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
}

def colourText(text):
    for color in COLOURS:
        text = text.replace("[[" + color + "]]", COLOURS[color])
    return text

def enterSchedule():
    flightList = []
    numFlights = int(input("Enter number of flights this Saturday(5 or more): "))
    while (numFlights < 5 or numFlights > 20):
        if (numFlights < 5):
            print(colourText("[[red]]Too few entries[[white]]"))
            numFlights = int(input("Enter number of flights this Saturday(5 or more): "))
        if (numFlights > 20):
            print(colourText("[[red]]Too many entries![[white]]"))
            numFlights = int(input("Enter number of flights this Saturday(5 or more): "))


    for i in range(numFlights):
        flightDetails = []
        dep = input("Enter Departure Time: ")
        flightDetails.append(dep)
        dest = input("Enter Flight Destination: ")
        flightDetails.append(dest)
        flightNum = input("Enter Flight Number: ")
        flightDetails.append(flightNum)
        gate = input("Enter Gate Number: ")
        flightDetails.append(gate)
        status = input("Enter Flight Status: ")
        flightDetails.append(status)
        
        flightList.append(flightDetails)

    fileHandler = open('flights.txt', 'w')
    for flightDetails in flightList:
        for x in range(5):
            fileHandler.write('%-18s' % flightDetails[x])
        fileHandler.write('\n')

    fileHandler.close()

    print(colourText("[[green]]file saved![[white]]"))
    con = input(colourText("[[green]]Press Enter to Continue[[white]]"))

def displaySchedule():
    fileHandler = open('flights.txt', 'r')
    content = fileHandler.read()
    print(colourText("[[yellow]]Departure         Destination       Flight No.        Gate              Status\n---------         -----------       ----------        ----              ------\n"))
    print(content)
    con = input(colourText("[[green]]Press Enter to Continue[[white]]"))

def searchFile():
    search = input(colourText("Search: [[yellow]]"))
    isFound = False

    searchFile = open("flights.txt", "r")
    for line in searchFile:
        if search in line:
            isFound = True
            print (line)
    if (isFound == False):
        print(colourText("[[red]]Entry not found![[white]]"))
    searchFile.close()
    con = input(colourText("[[green]]Press Enter to Continue[[white]]"))

def Menu():
    print(colourText("[[white]]Airport Schedule Program\n-------------------------\n\n\t1. Enter Schedule\n\t2. Display Schedule\n\t3. Search File\n\t[[red]]4. Exit[[white]]\n"))
    choice = int(input("What would you like to do?: "))
    
    if (choice == 1):
        enterSchedule()
    elif(choice == 2):
        displaySchedule()
    elif(choice == 3):
        searchFile()
    elif(choice == 4):
        exit()
    else:
        print(colourText("[[red]]Invalid Entry![[white]]"))
        Menu()
    Menu()

Menu()



