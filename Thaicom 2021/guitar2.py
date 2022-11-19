n,m,k = [int(x) for x in input().split()]
p= []
for i in range(n):
    a = [int(x) for x in input().split()]
    p.append(a)
sai = [int(x) for x in input().split()]

def findif(sai):
    diff = []
    for i in range(len(sai)-1):
        diff.append(p[sai[i]-1][sai[i+1]-1])
    return sum(diff)

best = findif(sai)
while k>0:
    best = findif(sai)
    for i in range(len(sai)):
        newsai = sai.copy()
        newsai = newsai[:i]+newsai[i+1:]
        if best < findif(newsai):
            pass
        else:
            best = findif(newsai)
            j = i
    sai = sai[:j]+sai[j+1:]
    k = k-1
print(best)
        
    

    





