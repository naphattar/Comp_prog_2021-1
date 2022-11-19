N,s0 = [int(x) for x in input().split()]
toon = [(0,s0)]
for i in range(N):
    s,t = [int(x) for x in input().split()]
    toon.append((t,s))
toon.sort()
def ab(x):
    if x>= 0:
        return x
    else:
        return (-1)*x        
toop = 0
for i in range(len(toon)-1):
    if ab(toon[i+1][1] - toon[i][1]) <= ab(toon[i+1][0] - toon[i][0]):
        toop = toop+1
print(toop)