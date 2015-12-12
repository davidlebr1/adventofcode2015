#Day 1

f = open('input.txt', 'r')
floor = 0
position = 0
findposition = False


for index, char in enumerate(f.read()):
    if char == '(':
        floor += 1
    else:
        floor += -1

    if floor == -1 and findposition is False:
        position = index + 1
        findposition = True

print ("The floor is : " + str(floor))
print ("The position is : " + str(position))
