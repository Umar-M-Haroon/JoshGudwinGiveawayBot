import random

f = open('subscriber-list.csv','r')
users = []
weights = []
for lineNumber, line in enumerate(f.readlines()):
    if lineNumber == 0:
        continue
    user = line.split(',')[0]
    users.append(user)
    subLevel = line.split(',')[2]
    subLevel = int(subLevel[-1])
    weights.append(subLevel)
print(random.choices(users,weights=weights)[0])
clientID = "jhv84dakqrupz132becnmpkmbewpso"
clientSecret = "shqt9ciwkwsn1n9s5vund0cdt3a8i2"