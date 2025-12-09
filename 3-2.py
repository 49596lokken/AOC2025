batteries = open("3.txt").read().splitlines()



def joltage(battery: list, length):

    if length == 1:
        return max(battery)
    digit = max(battery[:-(length-1)])
    index = battery.index(digit)
    return 10**(length -1) * digit + joltage(battery[index+1:], length-1)

ans = 0
for battery in batteries:
    battery = [int(i) for i in battery]
    jolt = joltage(battery, 12)
    print(jolt)
    ans += jolt

print(ans)
