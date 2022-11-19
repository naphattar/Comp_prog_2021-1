import numpy as np
n,X,Y = [int(a) for a in input().split()]
tar = np.zeros((n,3),int)
for i in range(n):
    x,y,c = [int(a) for a in input().split()]
    tar[(i,0)] += x
    tar[(i,1)] += y
    tar[(i,2)] += c
coor = np.sum(tar,axis =0)
def search(s):
    ans = []
    for i in range(len(s)):
        if s[i] == "1":
            ans.append(i)
    return ans
if coor[0] < X or coor[1]< Y :
    print(-1)
else:
    tata = np.zeros((2**n-1,3),int)
    for i in range(1,2**n):
        ans = search( "0"*(n-len(bin(i)[2:]))+bin(i)[2:])
        for j in ans:
            tata[i-1,0] += tar[j,0]
            tata[i-1,1] += tar[j,1]
            tata[i-1,2] += tar[j,2]
    x = tata[:,0]
    y = tata[:,1]
    c = tata[:,2]
    result = c[(x>= X) & (y>= Y)]
    print(np.min(result))
        
    
    
    



    




