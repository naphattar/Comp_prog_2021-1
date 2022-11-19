n  = int(input())
lis = [int(x) for x in input().split()]
lis.sort()
lis2 = [str(x) for x in lis]
p = " "
p = p.join(lis2)
print(p)
