#Day 6
f = open('input.txt', 'r')
arrinput = []
gridlight = [[0 for x in range(1000)] for x in range(1000)]
gridbrightness = [[0 for x in range(1000)] for x in range(1000)]
nblightopen = 0
totalbrightness = 0

def setLightAndBrightness(fromLight, throughlight, type):
    for i in range(int(fromlight[0]), int(throughlight[0])+1):
        for j in range(int(fromlight[1]), int(throughlight[1])+1):
            if type == 'on':
                gridlight[i][j] = 1
                gridbrightness[i][j] += 1
            elif type == 'off':
                gridlight[i][j] = 0
                if gridbrightness[i][j] > 0:
                    gridbrightness[i][j] -= 1
                else:
                    gridbrightness[i][j] = 0
            elif type == 'toggle':
                if gridlight[i][j] == 1:
                    gridlight[i][j] = 0
                elif gridlight[i][j] == 0:
                    gridlight[i][j] = 1
                gridbrightness[i][j] += 2

for light in f:
    arrinput.append(light.split())

for data in arrinput:
    if data[1] == 'on':
        fromlight = data[2].split(',')
        throughlight = data[4].split(',')
        setLightAndBrightness(fromlight, throughlight, 'on')

    if data[1] == 'off':
        fromlight = data[2].split(',')
        throughlight = data[4].split(',')
        setLightAndBrightness(fromlight, throughlight, 'off')

    if data[0] == 'toggle':
        fromlight = data[1].split(',')
        throughlight = data[3].split(',')
        setLightAndBrightness(fromlight, throughlight, 'toggle')

for x in range(0,1000):
    for y in range(0,1000):
        if gridlight[x][y] == 1:
            nblightopen += 1
        totalbrightness += gridbrightness[x][y]


print "Total light open : " + str(nblightopen)
print "Total brightness : " + str(totalbrightness)
