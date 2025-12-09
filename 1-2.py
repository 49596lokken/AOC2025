f = open("1.txt").read().splitlines()


ans = 0
pos = 50
for line in f:
    if line.startswith("L"):
        pos -= int(line[1:])
        while pos < 0:
            pos += 100
            ans += 1
    else:
        pos += int(line[1:])
        while pos > 99:
            pos -= 100
            ans += 1
        

print(ans)
    
