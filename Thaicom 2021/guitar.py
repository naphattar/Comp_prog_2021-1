n,m,k = [int(x) for x in input().split()]
p= []
for i in range(n):
    a = [int(x) for x in input().split()]
    p.append(a)
sai = [int(x) for x in input().split()]
diff = []
for i in range(m-1):
    diff.append(p[sai[i]-1][sai[i+1]-1])
diff.sort()
for i in range(k):
    diff.remove(diff[-1])
print(sum(diff))

   
