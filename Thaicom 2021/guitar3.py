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
supersai = [sai]
best = findif(sai)
while k>0:
    j = []
    for sai in supersai:
        best = findif(sai)
        for i in range(len(sai)):
            newsai = sai.copy()
            newsai = newsai[:i]+newsai[i+1:]
            if best < findif(newsai):
                pass
            else:
                best = findif(newsai)
                j.append(i)
        for l in j:
            deesai = sai.copy
            deesai = deesai[:j]+deesai[j+1:]
            supermansai = [deesai]

            
            
    k = k-1
print(best)