n,X,Y = [int(a) for a in input().split()]
tar = []
sumx,sumy =0,0
for i in range(n):
    x,y,c = [int(a) for a in input().split()]
    sumx += x
    sumy += y
    tar.append([x,y,c])
if sumx < X or sumy< Y :
    print(-1)
else:
    time = []
    for i in range(1,2**n):
        
        mn = "0"*(n-len(bin(i)[2:]))+bin(i)[2:]
        a = [tar[p][0] for p in range(len(mn)) if mn[p] == "1" ]
        b = [tar[p][1] for p in range(len(mn)) if mn[p] == "1" ]
        d = [tar[p][2] for p in range(len(mn)) if mn[p] == "1" ]
        x = sum(a)
        y =sum(b)
        c = sum(d)

        if x >= X and y >= Y:
            time.append(c)
        
    print(min(time))