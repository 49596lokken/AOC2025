dept = open("4.txt").read().splitlines()


dept = [[j for j in i] for i in dept]

def isValid(x,y):
    if y >= 0 and y < len(dept):
        return x >= 0 and x < len(dept[i])
    return False

ans = 0

finished = False
while not finished:
    finished = True
    for i in range(len(dept)):
        for j in range(len(dept[i])):
            if dept[i][j] != "@":
                continue
            surr = 0
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if isValid(i+y, j+x):
                        if dept[i+y][j+x] == "@":
                            surr += 1
            if surr < 5:
                ans += 1
                dept[i][j] = "."
                finished = False




print(ans)