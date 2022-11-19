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
        x,y,c = 0,0,0
        for j in range(len(mn)):
            if mn[j] == "1":
                x += tar[j][0]
                y += tar[j][1]
                c += tar[j][2]
        if x >= X and y >= Y:
            time.append(c)
        
    print(min(time))

    