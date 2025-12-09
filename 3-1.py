batteries = open("3.txt").read().splitlines()


ans = 0
for battery in batteries:
    battery = [int(i) for i in battery]
    firstindex = 0
    firstdigit = 0
    for i in range(len(battery)-1):
        if battery[i] > firstdigit:
            firstdigit = battery[i]
            firstindex = i
    seconddigit = 0
    for i in range(firstindex+1, len(battery)):
        if battery[i] > seconddigit:
            seconddigit = battery[i]
    
    ans += 10*firstdigit + seconddigit
print(ans)
