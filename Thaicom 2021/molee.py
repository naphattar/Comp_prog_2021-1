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
start,stop = 0 ,0
toop = 0
while start <= N:
    start = start+stop
    stop = 1
    while start+stop <= N:
        if ab(toon[start+stop][1] - toon[start][1]) <=  ab(toon[start+stop][0]-toon[start][0]):
            toop += 1
            break
        else:
             stop += 1
print(toop)