database = open("5.txt").read().split("\n\n")



freshranges, ingredients = database

freshranges = freshranges.splitlines()

freshranges = [[int(j) for j in i.split("-")] for i in freshranges]


print(freshranges)

# bubble sort the ranges based on lower bound

sorted = False
while not sorted:
    sorted = True
    i = 0
    while i < len(freshranges)-1:
        if freshranges[i][0] > freshranges[i+1][0]:
            temp = freshranges[i][:]
            freshranges[i] = freshranges[i+1][:]
            freshranges[i+1] = temp[:]
            sorted = False
        # Where they have the same start, merge the 2 into one range
        elif freshranges[i][0] == freshranges[i+1][0]:
            low = freshranges[i][0]
            high = max(freshranges[i][1],freshranges[i+1][1])
            freshranges = freshranges[:i] + freshranges[i+1:]
            freshranges[i] = [low, high]
            sorted = False
        i += 1
    
print(freshranges)

fixed = False
while not fixed:
    fixed = True
    i=0
    while i < len(freshranges)-1:
        if freshranges[i][1] >= freshranges[i+1][0]:
            low = freshranges[i][0]
            high = max(freshranges[i][1], freshranges[i+1][1])
            freshranges = freshranges[:i] + freshranges[i+1:]
            freshranges[i] = [low, high]
            fixed = False
        i += 1

print(freshranges)
ans = 0
lasthigh =  -1
for low,high in freshranges:
    ans += high-low + 1

print(ans)


