mark = 0
counter = 0
Msg = ["Redo the Assignment", "Resit the Test", "Resit the Exam", "You have passed the Module"]

while (mark != -1):
    passMark = 25
    mark = int(input("Enter Asssignment Mark(-1 to end): "))
    if (mark < passMark):
        print(Msg[counter])
        counter = 0
        continue
    counter += 1
    mark = int(input("Enter Test Mark(-1 to end): "))
    if (mark < passMark):
        print(Msg[counter])
        counter = 0
        continue
    counter += 1
    mark = int(input("Enter Exam Mark(-1 to end): "))
    passMark = 50
    if (mark < passMark):
        print(Msg[counter])
        counter = 0
        continue
    counter += 1
    print(Msg[counter])
    break
    
    


