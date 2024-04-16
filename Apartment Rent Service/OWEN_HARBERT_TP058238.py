#Owen Harbert
#TP058238

import os
from os import path 

print("Welcome!")

def start():

    welcomeChoice = input("\nWhat would you like to do:\n1. Open the Menu\n2. Rent an Apartment\n0. Exit\n\nSelect 1, 2 or 0: ")

    if welcomeChoice == "1":
        menu()
    elif welcomeChoice == "2":
        registration()
    elif welcomeChoice == "0":
        exit()
    else:
        con = input("Input invalid! Try again (Press Enter to continue")
        start()

def checkFilebase():
    
    try:
        os.makedirs("C:/RentSystem/Apartments/")
    except OSError:
        start()
    else:
        createFilebase()
        start()
        
def createFilebase():
    
    availableRooms = []
    aRooms = ["1","2"]
    bRooms = ["1","2","M"]
    aptTypes = ["A","B"]
    
    os.makedirs('C:/RentSystem/Accounts/')

    for aptType in aptTypes:
        
        path = "C:/RentSystem/Apartments/"+aptType+'/'

        os.makedirs(path)

        if aptType == 'A':
            rooms = aRooms
        elif aptType == 'B':
            rooms = bRooms

        for apt in range(1,21,1):
        
            aptPath = path+str(apt).zfill(2)+"/"

            os.makedirs(aptPath)
            os.chdir(aptPath)
            
            for room in rooms:
                roomNum = aptType+str(apt).zfill(2)+"-"+room
            
                f = open(room+'.txt','w')
                f.write("room:"+roomNum+"\noccupant:none")
                f.close()

                availableRooms.append(roomNum)

    f = open("C:/RentSystem/Apartments/AvailabilityList.txt","w")
    for room in availableRooms:
        f.write(room+"\n")
    f.close()

    f = open('C:/RentSystem/Accounts/CheckedOut.txt','w')
    f.write("TP number:Password:Full Name:Months Stayed:Total Paid\n-----------------------------------------------------\n")
    f.close()

def registration():
    
    print("\nCreate an account\n------------------")
    
    tpNum = str(input("Enter your TP number: "))
    _tpNum = str(input("Confirm TP number: "))

    while tpNum != _tpNum:
        print("Passwords don't match")
        tpNum = str(input("Enter your TP number: "))
        _tpNum = str(input("Confirm TP number: "))

    name = str(input("Full Name (first name and surname): "))

    password = str(input("Enter a Password: "))
    _password = str(input("Confrim Password: "))

    while password != _password:
        print("Passwords don't match")
        password = str(input("Enter a Password: "))
        _password = str(input("Confrim Password: "))
    
    try:
        path.exists('C:/RentSystem/Accounts/'+tpNum+'.txt')
    except OSError:
        print("File already exists")
        con = input("Press enter to return to start menu")
        start()

    os.chdir('C:/RentSystem/Accounts/')

    rent(tpNum, password, name)

    menu()

def rent(tpNum:str, password:str, name:str):

    aptType = str(input("\nSelect apartment type A or B: "))

    if aptType == "A":
        print("\nApartment type A, single bedroom selected")
        rentFee = int(400)
        roomType = 1

        room, availableRooms = roomSelect(aptType, roomType, tpNum)

        prompt = input("\nWould you like and internet subscription?\n1 for yes or 2 for no: ")

        if prompt == '1':
            print("\nAdded internet subscription")
            internetFee = int(50)
        elif prompt == '2':
            print("\nNo internet subscription")
            internetFee = int(0)
        else:
            invalid = input("\nInput invalid! Press enter to try again")
            rent(tpNum)
    elif aptType == "B":
        selection = input("\nWould you like\n\n1. Single bedroom\n2. Master bedroom\nSelect 1 or 2: ")
        
        if selection == "1":
            print("\nApartment type B, single bedroom selected")
            roomType = 1
            rentFee = int(300)
        elif selection == "2":
            print("\nApartment type B, master bedroom selected")
            roomType = 2
            rentFee = int(500)
        else:
            invalid = input("\nInput invalid! Press enter to try again")
            rent(tpNum)
        
        room, availableRooms = roomSelect(aptType, roomType, tpNum)

        prompt = input("\nWould you like and internet subscription?\n1 for yes or 2 for no: ")

        if prompt == '1':
            print("\nAdded internet subscription")
            internetFee = int(40)
        elif prompt == '2':
            print("\nNo internet subscription")
            internetFee = int(0)
        else:
            invalid = input("\nInput invalid! Press enter to try again")
            rent(tpNum)

    fullRent, fullTotal = calculateRent(rentFee, internetFee)

    amountPaid = payment(fullTotal, fullRent)

    aptNum, _room = room.lstrip(aptType).split('-')
    aptDir = 'C:/RentSystem/Apartments/'+aptType+'/'+aptNum+'/'
    
    f = open(tpNum+'.txt','w')
    f.write(tpNum+":"+password+"\nName:"+name+"\nRoom:"+room+"\nTotal Bill:RM"+str(fullTotal)+"\nTotal Paid:RM"+str(amountPaid))
    f.close()

    f = open('C:/RentSystem/Accounts/AccountList.txt','a')
    f.write(tpNum+':'+name+'\n')
    f.close()

    f = open(aptDir+_room+'.txt','w')
    f.write("room:"+room)
    f.write("\noccupant:"+tpNum)
    f.close()
    
    f = open("C:/RentSystem/Apartments/AvailabilityList.txt","w")
    for rooms in availableRooms:
        f.write(rooms)
    f.close()

def roomSelect(apartment:str, room:int, tpNum:str):

    availableRooms = []

    f = open('C:/RentSystem/Apartments/AvailabilityList.txt','r')
    availableRooms = f.readlines()
    f.close()

    print("\nRoom Selection\n--------------")
    
    print("Next Available Room: ")
    
    if apartment == 'A':
        
        for i in availableRooms:
            if i.startswith("A"):
                print(i.rstrip("\n"), sep="", end=" | ", flush = True)
                roomNum = i.rstrip("\n")
                break
            else:
                continue

    elif apartment == 'B' and room == 1:
        
        for i in availableRooms:
            if i.startswith("B") and not i.endswith("M\n"):
                print(i.rstrip("\n"), sep="", end=" | ", flush = True)
                roomNum = i.rstrip("\n")
                break
            else:
                continue

    elif apartment == 'B' and room == 2:
        
        for i in availableRooms:
            if i.startswith("B") and i.endswith("M\n"):
                print(i.rstrip("\n"), sep="", end=" | ", flush = True)
                roomNum = i.rstrip("\n")
                break
            else:
                continue

    print("Your room allocation is: ", str(roomNum))

    try:
        availableRooms.remove(roomNum+'\n')
    except ValueError:
        invalid = input("Invalid input! Press enter to try again")
        roomSelect(apartment, room, tpNum)

    return roomNum, availableRooms

def calculateRent(rent:int, internet:int):
    
    deposit = 100
    monthlyRate = rent + internet
    semesterTotal = monthlyRate * 5
    totalBill = semesterTotal + deposit
    
    print('\n\tBill\n\t----')
    print('\tRoom Rent/semester--------------------RM'+str(rent*5)+'.00')
    print('\tInternet Subscription/per semester----RM'+str(internet*5)+'.00')
    print('\tDeposit-------------------------------RM'+str(deposit)+'.00')
    print('\t===============================================')
    print('\tRent Total----------------------------RM'+str(semesterTotal)+'.00')
    print('\tTotal Bill----------------------------RM'+str(totalBill)+'.00')
    print('\t===============================================')

    return semesterTotal, totalBill

def payment(total:int, rent:int):
    
    prompt = input("\nChoose payment plan\n1. Full payment\n2. Partial payment\nSelection: ")

    minimum = rent/2 + 100

    if prompt == '1':
        print("\nFull payment plan selected!\n\nProceed to pay RM"+str(total)+" to the tenant.")
        con = input("Press Enter to continue")
        amount = total
    elif prompt == "2":
        print("\nPartial payment plan selected!\nFirst instalment must be a minimum of RM"+str(minimum)+", including the RM100 deposit.")
        amount = int(input("\nInput amount of first instalment: "))

        if amount < minimum:
            invalid = input("Amount entered is less than the minimum amount.\nPress Enter to try again")
            payment(total, rent)
        elif amount >= total:
            invalid = input("Amount more than or equal to full payment.\nPress Enter to try again")
            payment(total, rent)
        else:
            print("Proceed to pay first instalment of RM"+str(amount)+" to the tenant.")
            con = input("You have RM"+str(total - amount)+" left to pay.\nPress Enter to continue")
    else:
        invalid = input("Input invalid.\nPress Enter to try again")
        payment(total, rent)

    return amount

def menu():

    print("\nWelcome\nPlease select an option:\n-------------------------\n")

    option = input("1. Checkout\n2. Print Accounts Information\n3. Search\n4. Return to start\n0. Exit\n\nSelection: ")

    if option == '1':
        tpNum = login()
        checkout(tpNum)
    elif option == '2':
        info()
    elif option == '3':
        search()
    elif option == '4':
        os.chdir('C:/RentSystem/')
        start()
    elif option == '0':
        exit()
    else:
        print("Option Invalid Try again")
        option = input("1. Checkout\n2. Print account info\n3. Search\n4. Log out\n0. Exit\n\nSelection: ")
        menu()

def login():
    
    print("\nLogin\n-----\n")
    
    tpLogin = str(input("Enter your TP number: "))

    try:
       os.chdir('C:/RentSystem/Accounts/')
       f = open(tpLogin+'.txt','r')
    except:
        print("\nInput incorrect or file does not exist")
        menu()

    f.close()

    passwordLogin = str(input("Enter a Password: "))

    _login = tpLogin+":"+passwordLogin+"\n"

    f = open(tpLogin+'.txt','r')
    login = f.readline()
    name = f.readline().lstrip("Name:")
    f.close()
    
    if login == _login:
        return tpLogin
    else:
        print("Password incorrect! Retry")
        login()

def checkout(tpNum:str):
    
    print("Checkout Menu\n-------------")

    prompt = input("1. Proceed with Checkout\n2. Back to Menu\nSelection: ")

    if prompt == "1":
        
        months = int(input("Input number of months stayed: "))

        f = open(tpNum+'.txt','r')
        _password = f.readline().rstrip("\n")
        _name = f.readline().rstrip("\n")
        _room = f.readline().rstrip("\n")
        _total = f.readline().rstrip("\n")
        _paid = f.readline().rstrip("\n")
        f.close()

        password = _password.lstrip(tpNum+":")
        name = _name.lstrip("Name:")
        room = _room.lstrip("Room:")
        total = int(_total.lstrip("Total Bill:RM"))
        paid = int(_paid.lstrip("Total Paid:RM"))
        deposit = 100
        rentPaid = paid - deposit
        rent = (total - deposit) / 5
        due = rent * months

        if (rentPaid >= due):
            print("Please collect your RM100 deposit and your refund of RM"+str(rentPaid - due)+" from the tenant.")
        elif (rentPaid < due):
            print("Please collect your RM100 deposit and pay RM"+str(due - rentPaid)+" to settle your bill at the tenant")

        f = open('C:/RentSystem/Accounts/CheckedOut.txt','a')
        f.write(tpNum+":"+password+":"+name+":"+str(months)+":"+str(due)+"\n")
        f.close()
        
        os.remove(tpNum+'.txt')

        f = open('C:/RentSystem/Apartments/AvailabilityList.txt','r')
        availableRooms = f.readlines()
        f.close()

        availableRooms.insert(0, room)

        f = open('C:/RentSystem/Apartments/AvailabilityList.txt','w')
        for rooms in availableRooms:
            f.write(rooms+'\n')
        f.close()
    elif prompt == "2":
        menu()
    else:
        invalid = input("Input invalid, press enter to try again")
        checkout(tpNum)

    con = input("\nPress enter to go back to Menu")
    
    menu()

def info():
    
    totalRent = 0
    totalRecievable = 0
    numAccounts = 0

    f = open('C:/RentSystem/Accounts/AccountList.txt','r')
    accounts = f.readlines()
    f.close()

    for i in accounts:
        numAccounts += 1
        tpNum, name = i.split(":")
        _f = open('C:/RentSystem/Accounts/'+tpNum+'.txt','r')
        _f.readline()
        _f.readline()
        _f.readline()
        recievable = int(_f.readline().lstrip('Total Bill:RM'))
        rent = int(_f.readline().lstrip('Total Paid:RM'))
        _f.close()

        totalRecievable += int(recievable)
        totalRent += int(rent)

    f = open('C:/RentSystem/Accounts/CheckedOut.txt','r')
    checked = f.readlines()
    checked.pop(0)
    checked.pop(0)
    f.close()
    for line in checked:
        null, _rent = line.rsplit(":",1)
        print(_rent)
        rent = _rent.rstrip('\n')
        totalRent += int(rent)

    totalDeposit = numAccounts * 100

    print("\t==============================================")
    print("\tTotal deposits collected:-----------RM"+str(totalDeposit)+".00")
    print("\tTotal rent amount collected:--------RM"+str(totalRent)+".00")
    print("\tTotal amount collectible:-----------RM"+str(totalRecievable)+".00")
    print("\t==============================================")

    con = input("\nPress enter to go back to Menu")
    menu()

def search():
    
    print("Please input search method\n1. Name or TP number\n2. Apartment Unit Number\n0. Return to Menu")
    prompt = input("Select from 0 to 2: ")

    found = False

    if prompt == "1":
        
        search = input("Please enter full name or TP number: ")
        searchFile = open('C:/RentSystem/Accounts/AccountList.txt','r')
        _searchFile = open('C:/RentSystem/Accounts/CheckedOut.txt','r')
        
        for line in searchFile:
            if search in line:
                found = True
                tpNum, name = line.rstrip("\n").split(":")
                checkedOut = False
            else:
                continue
        
        for line in _searchFile:
            if search in line:
                found = True
                tpNum, null = line.rstrip("\n").split(":", 1)
                checkedOut = True
            else:
                continue
        
        searchFile.close()
        _searchFile.close()
        
        if found == True:
            displayAccount(tpNum, checkedOut)
        elif found == False:
            print("Either input is incorrect or account doesn't exist")
            invalid = input("Press enter to return to menu")
            menu()
    
    elif prompt == "2":
        part1 = input("Please enter apartment type(A or B): ")
        
        if part1 == "A" or part1 == "B":
            part2 = int(input("Please enter apartment number(1 to 20): "))
            
            if part2 > 0 and part2 <= 20 and part1 == "A":
                part3 = int(input("Please enter room number(1 or 2): "))
                
                if part3 > 0 and part3 <= 2:
                    search = part1+str(part2).zfill(2)+'-'+str(part3)
                else:
                    invalid = input("Input invalid! Press enter to try again")
                    search()
            elif part2 > 0 and part2 <= 20 and part1 == "B":
                
                part3 = input("Please enter room number(1, 2 or M): ")
                
                if part3 == '1' or part3 == "2" or part3 == "M":
                    search = part1+str(part2).zfill(2)+'-'+part3
                else:
                    invalid = input("Input invalid! Press enter to try again")
                    search()
            else:
                invalid = input("Input invalid! Press enter to try again")
                search()
        else:
            invalid = input("Input invalid! Press enter to try again")
            search()

        searchFileName = part1+'/'+str(part2).zfill(2)+'/'+str(part3)+'.txt'
        searchFile = open('C:/RentSystem/Apartments/'+searchFileName,'r')
        searchFile.readline()
        tpNum = searchFile.readline().lstrip("occupant:")
        searchFile.close()
        if tpNum == "none\n":
            print("Room unoccupied!")
            con = input("Press enter to return to menu")
            menu()
        else:
            displayAccount(tpNum.rstrip("\n"), False)
    
    elif prompt == "0":
        menu()
    else:
        invalid = input("Input invalid! Press enter to try again")
        search()

    con = input("Press enter to return to menu")
    menu()

def displayAccount(tpNum:str, checkedOut:bool):
    
    if checkedOut == False:
        f = open('C:/RentSystem/Accounts/'+tpNum+'.txt','r')
        info = f.readlines()
        f.close()
        info.pop(0)
        print("TPnumber: "+tpNum)
        for i in info:
            print(i)
    elif checkedOut == True:
        f = open('C:/RentSystem/Accounts/CheckedOut.txt','r')
        for line in f.readlines():
            if tpNum in line:
                null, name, months, paid = line.rstrip("\n").rsplit(":",3)
                break
            else:
                continue
        
        f.close()
        
        print("TPnumber: "+tpNum+"\nName: "+name+"\nMonths Stayed: "+months+"\nTotal Paid: RM"+paid)

checkFilebase()