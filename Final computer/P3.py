def pattern1(N):
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            ans[i] = ans[i] + [0]
    sum = 1
    for i in range(N):
        for j in range(N-1,N-i-2,-1):
            ans[i][j] += sum
            sum += 1
    return ans

def pattern2(N):
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            ans[i] = ans[i] + [0]
    sum = 1
    for i in range(N):
        for j in range(N-i):
            ans[j][i] += sum
            sum += 1
    return ans
print(pattern2(5))