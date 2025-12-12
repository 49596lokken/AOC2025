f = open("6.txt").read().splitlines()



problems = []
problem_indices = []
for i in range(len(f[-1])):
    if f[-1][i] != " ":
        problem_indices.append(i)


ans = 0
for i in range(len(problem_indices)):
    if i == len(problem_indices)-1:
        nextone = len(f[0])+1
    else:
        nextone = problem_indices[i+1]
    problem_ans = int(f[-1][problem_indices[i]] == "*")
    for j in range(nextone-2, problem_indices[i]-1, -1):
        num = ""
        for k in range(len(f)-1):
            if f[k][j] == " ":
                continue
            else:
                num += f[k][j]
        num = int(num)
        if f[-1][problem_indices[i]] == "*":
            problem_ans *= num
        else:
            problem_ans += num
    ans += problem_ans

print(ans)



