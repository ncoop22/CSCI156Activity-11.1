__author__ = 'Nickolas'


Abbrevations = {'Thot': 'That hoe over there','SEC': 'South Eastern Conference','ABSP': 'Association of British Scrabble Players','AEA': 'Aussie Elite Assassins','D4P':'Double Four Patch'}
#that hoe over there, South Eastern Conference, Association of British Scrabble Players, Aussie Elite Assassins, Double Four Patch

print(Abbrevations['SEC'])

print(Abbrevations.get('ABSP'))

for abv in Abbrevations:
    print(abv+"\n")

for abv in Abbrevations:
    if abv == "Thot":
        print("I like"+" "+Abbrevations['Thot'])
    else:
        continue




