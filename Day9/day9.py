#Day9
import itertools

f = open('input.txt', 'r')
arraycity = []
mydict = {}
shortestdistance = 10000
longestdistance = 1

for d in f:
    mydict[(d.split()[0]), d.split()[2]] = d.split()[4]
    if d.split()[0] not in arraycity:
        arraycity.append(d.split()[0])

    if d.split()[2] not in arraycity:
        arraycity.append(d.split()[2])

for p in list(itertools.permutations(arraycity, len(arraycity))):

    if (p[0],p[1]) in mydict:
        va1 = mydict[p[0],p[1]]
    else:
        va1 = mydict[p[1],p[0]]

    if (p[1],p[2]) in mydict:
        va2 = mydict[p[1],p[2]]
    else:
        va2 = mydict[p[2],p[1]]

    if (p[2],p[3]) in mydict:
        va3 = mydict[p[2],p[3]]
    else:
        va3 = mydict[p[3],p[2]]

    if (p[3],p[4]) in mydict:
        va4 = mydict[p[3],p[4]]
    else:
        va4 = mydict[p[4],p[3]]

    if (p[4],p[5]) in mydict:
        va5 = mydict[p[4],p[5]]
    else:
        va5 = mydict[p[5],p[4]]

    if (p[5],p[6]) in mydict:
        va6 = mydict[p[5],p[6]]
    else:
        va6 = mydict[p[6],p[5]]

    if (p[6],p[7]) in mydict:
        va7 = mydict[p[6],p[7]]
    else:
        va7 = mydict[p[7],p[6]]

    distance = int(va1)+int(va2)+int(va3)+int(va4)+int(va5)+int(va6)+int(va7)
    if distance < shortestdistance:
        shortestdistance = distance

    if distance > longestdistance:
        longestdistance = distance


print("Shortest distance : " + str(shortestdistance))
print("Longest distance : " + str(longestdistance))
