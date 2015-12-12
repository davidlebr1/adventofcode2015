#Day 5
f = open('input.txt', 'r')
vowels = ['a', 'e', 'i', 'o', 'u']
letterrestriction = ['ab', 'cd', 'pq', 'xy']
occurence = False
iscontainletter = False
nicestring = 0
nicestring2 = 0
lastchar = ''
ispair = False
between = False
numberofvowels = 0

for sentence in f.read().split():

    for index, c in enumerate(sentence):
        if index <= len(sentence)-3:
            if c == sentence[index+2]:
                between = True
        if index <= len(sentence)-2:
            if sentence.count(sentence[index]+sentence[index+1]) >= 2:
                ispair = True

        if c in vowels:
            numberofvowels += 1
        if lastchar == c:
            occurence = True
        lastchar = c

    for s in letterrestriction:
        if s in sentence:
            iscontainletter = True

    if numberofvowels >= 3 and occurence == True and iscontainletter == False:
        nicestring += 1

    if ispair == True and between == True:
        nicestring2 += 1

    numberofvowels = 0
    occurence = False
    iscontainletter = False
    lastchar = ''
    between = False
    ispair = False

print ("Number of nicestring #1: " + str(nicestring))
print ("Number of nicestring #2 : " + str(nicestring2))
