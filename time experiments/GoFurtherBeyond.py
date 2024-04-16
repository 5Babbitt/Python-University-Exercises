import time

nextNum = 0
currNum = 1
preNum = 0
counter = 7100
delay = 0.001

time.sleep(1.4)
print("And this...")
time.sleep(1.8)
print("Is...")
time.sleep(0.9)
print("To go even further beyond!")
time.sleep(4)
for i in range(counter):
    nextNum = preNum + currNum
    preNum = currNum
    currNum = nextNum
    print("A", sep="", end= "", flush= True)
    time.sleep(delay)
print("H!", sep="", end= "", flush= True)
