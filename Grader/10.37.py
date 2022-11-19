n = int(input())
faculty = {}
for i in range(n):
    fal,num = input().split()
    faculty[fal] = int(num)
m = int(input())
data = []
for i in range(m):
    id,score,f1,f2,f3,f4 = input().split()
    data.append([float(score),id,f1,f2,f3,f4])
data.sort()
answer = {}
for i in range(m-1,-1,-1):
    j = 2
    while faculty[data[i][j]] <= 0:
        j = j+1
    answer[data[i][1]] = data[i][j]
    faculty[data[i][j]] = faculty[data[i][j]]-1
for d in sorted(answer):
    print(d,answer[d])


