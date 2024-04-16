sPrice = float(input('Enter selling price: '))
bPrice = float(input('Enter buying price: '))

if (sPrice < bPrice):
    print('You have made a loss')
elif(sPrice > bPrice):
    print('You have made a profit')
else:
    print('You have made neither loss nor profit')