import time

nextNum = 0
currNum = 1
preNum = 0
counter = int(input("Enter sequence length: "))
delay = 0.01

print(preNum)
time.sleep(delay)
print(currNum)
time.sleep(delay)
for i in range(counter):
    nextNum = preNum + currNum
    preNum = currNum
    currNum = nextNum
    print(currNum)
    time.sleep(delay)

next = str(input("Press Enter to finish"))
