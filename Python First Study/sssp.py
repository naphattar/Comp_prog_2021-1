n,m = [int(x) for x in input().split()]
import numpy as np
f = np.zeros((n,n), int)
print(f)
for i in range(m):
    a,b,d = [int(x) for x in input().split()]
    f[a-1,b-1] += d
print(f)
ans = [0]
for i in range(1,n):
    dis = 0
    if f[0,i] >0 :
        dis = f[0,i]
    else:
        
    


