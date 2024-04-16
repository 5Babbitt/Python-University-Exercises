distanceTime = []
speed = []

def getDistanceTime():
    distance = int(input("Enter distance ran in metres(m) [-1 to end]: "))

    while distance != -1:
        distanceTime.append(distance)
        time = float(input("Enter time taken in seconds(s): "))
        distanceTime.append("%.2f" % time)
        distance = int(input("Enter distance ran in metres(m) [-1 to end]: "))

def calculateSpeed():
    for i in range(0, len(distanceTime), 2):
        distance = int(distanceTime[i])
        time = float(distanceTime[i + 1])
        
        _speed = distance / time
        speed.append("%.2f" % _speed)

def odd(n):
    return 2*n + 1

def even(n):
    return 2*n

def trialRecord():
    getDistanceTime()
    calculateSpeed()

    fHand = open('Trial_Record.txt', 'w')
    fHand.write("Distance(m)    Time(s)        Speed(m/s)     ")
    
    for i in range(0, int(len(distanceTime)/2)):
        fHand.write('\n%-15s' % distanceTime[even(i)])
        fHand.write('%-15s' % distanceTime[odd(i)])
        fHand.write('%-15s' % speed[i])

trialRecord()