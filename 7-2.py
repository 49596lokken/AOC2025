f = open("7.txt").read().splitlines()


for i in range(len(f)):
    f[i] = [j for j in f[i]]

beams = []
beams.append((0, f[0].index("S"), 1))
f[0][f[0].index("S")] = "."

def addbeam(beam, beams):
    for i, b in enumerate(beams):
        if (b[0],b[1]) == (beam[0],beam[1]):
            beams[i] = (b[0], b[1], b[2]+beam[2])
            return
    beams.append(beam)

ans = 0
while beams:
    beam = beams[0]
    if beam[0] == len(f):
        beams = beams[1:]
        ans += beam[2]
        continue
    match f[beam[0]][beam[1]]:
        case "^":
            addbeam((beam[0], beam[1]-1, beam[2]), beams)
            addbeam((beam[0], beam[1]+1, beam[2]), beams)
            beams = beams[1:]
        case ".":
            addbeam((beam[0]+1, beam[1], beam[2]), beams)
            beams = beams[1:]


print(ans)

    