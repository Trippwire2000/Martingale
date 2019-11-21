#!/bin/python3
print('\nMartingale counter')
basebet = int(input('\nWhat is the base bet?  - '))
losestreak = int(input('How many losses in a row do you want to calculate? - '))
print('\n')
tot = 0
for i in range(1, (losestreak + 1)):
    if i == 1:
        tot = basebet
    else:
        basebet *= 2
    print(basebet)
    tot = tot + basebet
print('\nTotal balance required is ' + str(tot))

