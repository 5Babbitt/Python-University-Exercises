#part 1, Input car number, labour charge and cost of parts then add to list
service = []
bill = []

def getDailyService():
    tempService = []
    carNum = input("Enter first car number (-1 to end): ")

    while (carNum != "-1"):
        charge = float(input("Enter labour charge: "))
        cost = float(input("Enter cost of parts: "))

        service.append(carNum)
        service.append("%.2f" % charge)
        service.append("%.2f" % cost)

        carNum = input("Enter next car number (-1 to end): ")

def calculateDailyBill():
    for i in range(0, len(service), 3):
        cost = float(service[i + 1])
        charge = float(service[i + 2])

        dTotal = cost + charge
        total = dTotal + dTotal * (6/100)

        bill.append("%.2f" % total)

def weeklyService():

    for i in range(7):
        print("Services done on day", i+1)

        getDailyService()
    
    calculateDailyBill()

    f = open('Weekly_Service.txt', 'w')
    f.write('Car Number     Labour Charge  Cost of parts  Bill\n----------     -------------  -------------  ----')
    for i in range(0, len(service), 3):
        f.write('\n%-15s' % service[i])
        f.write('%-15s' % service[i + 1])
        f.write('%-15s' % service[i + 2])
        f.write('%-15s' % bill[int(i / 3)])

weeklyService()