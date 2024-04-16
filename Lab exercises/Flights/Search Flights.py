def searchFile():
    search = input("Search: ")

    searchFile = open("Flights.txt", "r")
    for line in searchFile:
       if search in line: 
            print (line)
    searchFile.close()
    con = input("Press Enter to Continue")

searchFile()


