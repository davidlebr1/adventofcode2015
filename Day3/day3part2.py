#adventofcode
#day 3 part 2

f = open('input.txt','r')
mapsanta = [[0 for x in range(500)] for x in range(500)]
maprobotsanta = [[0 for x in range(500)] for x in range(500)]
houses = 0
santai = 0
santaj = 0
roboti = 0
robotj = 0

#starting location [0][0]
mapsanta[santai][santaj] = 1
maprobotsanta[roboti][robotj] = 1

for index, c in enumerate(f.read()):

    #pair santa turn
    if index % 2 == 0:
        if c == '^':
             santaj += 1
        if c == '>':
            santai += 1
        if c == '<':
            santai += -1
        if c == 'v':
            santaj += -1
        mapsanta[santai][santaj] += 1
    else:
        #unpair robot turn
        if c == '^':
             robotj += 1
        if c == '>':
            roboti += 1
        if c == '<':
            roboti += -1
        if c == 'v':
            robotj += -1
        maprobotsanta[roboti][robotj] += 1


for i in range(500):
    for j in range(500):
        if mapsanta[i][j] > 0:
            houses += 1
        elif maprobotsanta[i][j] > 0:
            houses += 1

print ("Number of houses : " + str(houses))
