f = open("6.txt").read().splitlines()


for i in range(len(f)):
    while "  " in f[i]:
        f[i] = f[i].replace("  ", " ")
    if f[i][-1] == " ":
        f[i] = f[i][:-1]
    f[i] = f[i].split(" ")
    if "" in f[i]:
        f[i].remove("")
    if i+1<len(f):
        f[i] = [int(j) for j in f[i]]

print(f)

ans = 0
for j in range(len(f[0])):
    if f[-1][j] == "*":
        prod = 1
        for k in range(len(f)-1):
            prod *= f[k][j]
        ans += prod
    else:
        for k in range(len(f)-1):
            ans += f[k][j]

print(ans)
