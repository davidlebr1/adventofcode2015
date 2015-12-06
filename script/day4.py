#Day 4

import hashlib

secretkey = "ckczppom"
finded = False
answer = ""

for i in range(0,10000000):
    if hashlib.md5(secretkey+str(i)).hexdigest().startswith("00000") and finded is False:
        print ("Answer for 5 zero is : " + str(i))
        finded = True
    if hashlib.md5(secretkey+str(i)).hexdigest().startswith("000000"):
        print ("Answer with 6 zero is : " + str(i))
        break
