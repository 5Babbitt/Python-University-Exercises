def enterSchedule():
    flightList = []
    numFlights = int(input("Enter number of flights this Saturday(5 or more): "))
    while (numFlights < 5 or numFlights > 20):
        if (numFlights < 5):
            print("Too few entries")
            numFlights = int(input("Enter number of flights this Saturday(5 or more): "))
        if (numFlights > 20):
            print("Too many entries!")
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
    fileHandler.write("Departure         Destination       Flight No.        Gate              Status\n---------         -----------       ----------        ----              ------\n")
    for flightDetails in flightList:
        for x in range(5):
            fileHandler.write('%-18s' % flightDetails[x])
        fileHandler.write('\n')

    fileHandler.close()

    print("file saved!")
enterSchedule()