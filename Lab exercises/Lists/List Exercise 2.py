firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']

firstList.extend(secondList)

firstList.sort(reverse=True)
for game in firstList:
    print(game)
