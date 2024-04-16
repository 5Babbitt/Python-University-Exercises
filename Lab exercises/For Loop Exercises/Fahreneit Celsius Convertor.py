import time

for i in range(15):
    F = float(input("\nInput temperature in fahrenheit: "))
    C = (F - 32) * 5 / 9
    print("\nTemperature is %.1f" % C ,"degrees Celsius")

time.sleep(0.5)
print("\nAll temperatures processed!")