#Day 8

f = open('input/day8.txt', 'r')
totallencode = 0
totallendata = 0
totallenpart2 = 0

for line in f:
    totallencode += len(line)
    totallendata += len(line.decode('string-escape')) - 2
    line = line.replace('\\','\\\\')
    line = line.replace('"','\\"')
    totallenpart2 += len(line) + 2

print "Part 1 : " + str(totallencode - totallendata)
print "Part 2 : " + str(totallenpart2 - totallencode)
