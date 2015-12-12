#Day 2

f = open('input.txt','r')
feetwrappingpaper = 0
feetribbon = 0
minimum = 0

for eq in f.read().split():
    lwh = eq.split('x')
    lwh = map(int, lwh)

    lw = lwh[0]*lwh[1]
    wh = lwh[1]*lwh[2]
    hl = lwh[2]*lwh[0]
    minimum = min(lw,wh,hl)
    feetwrappingpaper += 2*lw+2*wh+2*hl+minimum

    ribbon = 2*sorted(lwh)[0] + 2*sorted(lwh)[1]
    bow = lwh[0]*lwh[1]*lwh[2]
    feetribbon += ribbon + bow

print ("Feet of wrapping paper : " + str(feetwrappingpaper))
print("Feet of ribbon : " + str(feetribbon))
