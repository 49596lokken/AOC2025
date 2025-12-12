f = open("7.txt").read().splitlines()



for i in range(len(f)):
    f[i] = [j for j in f[i]]

beams = []
beams.append((0, f[0].index("S")))
f[0][f[0].index("S")] = "."

splits = 0
while beams:
    beam = beams[0]
    if beam[0] == len(f):
        beams = beams[1:]
        continue
    match f[beam[0]][beam[1]]:
        case "^":
            beams.append((beam[0], beam[1]-1))
            beams.append((beam[0], beam[1]+1))
            beams = beams[1:]
            splits += 1
        case ".":
            beams[0] = (beam[0]+1, beam[1])
            f[beam[0]][beam[1]] = "|"
        case "|":
            beams = beams[1:]

print(splits)

    