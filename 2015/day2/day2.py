packages = []
with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        l,w,h = line.split('x')
        packages.append([int(l),int(w),int(h)])

totalSquare = 0
feetRibbon = 0
for pack in packages:
    lw = pack[0]*pack[1]
    wh = pack[1]*pack[2]
    hl = pack[2]*pack[0]
    extraPaper = min(lw,wh,hl)
    totalSquare += 2*(lw+wh+hl)+extraPaper
    feetRibbon += 2*(min(pack[0]+pack[1], pack[0]+pack[2], pack[1]+pack[2]))
    feetRibbon += pack[0]*pack[1]*pack[2]

print("#Day2 - Part 1:",totalSquare)
print("#Day2 - Part 2:", feetRibbon)
