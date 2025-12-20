f = open("8.txt").read().splitlines()


for i in range(len(f)):
    f[i] = [int(j) for j in f[i].split(",")]

def point_dist(a, b):
    d = 0
    for i in range(3):
        d += (a[i]-b[i])**2
    return d

distances = dict()
for i in range(len(f)):
    for j in range(i+1, len(f)):
        distances[(i,j)] = point_dist(f[i], f[j])

sorted_distances = sorted([i for i in distances], key=(lambda x: distances[x]))

circuits = [[i] for i in range(len(f))]

for connection in sorted_distances:
    for circuit in circuits:
        if connection[0] in circuit:
            # Have found where the first one is
            for circuit2 in circuits:
                # Find the second
                if connection[1] in circuit2:
                    # Have found 
                    if circuit != circuit2:
                        circuit.extend(circuit2)
                        circuits.remove(circuit2)
                    break
            break
    if len(circuits) == 1:
        b1 = f[connection[0]]
        b2 = f[connection[1]]
        print(b1[0] * b2[0])
        break
        
    



    