#adventofcode
#day 3 part 1
f = open('input.txt', 'r')
mapsanta = [[0 for x in range(500)] for x in range(500)]
houses = 0
i = 0
j = 0

#starting location [0][0]
mapsanta[i][j] += 1

for c in f.read():

    if c == '^':
         j += 1
    if c == '>':
        i += 1
    if c == '<':
        i += -1
    if c == 'v':
        j += -1

    mapsanta[i][j] += 1

for i in range(500):
    for j in range(500):
        if mapsanta[i][j] > 0:
            houses += 1

print ("Number of houses : " + str(houses))
