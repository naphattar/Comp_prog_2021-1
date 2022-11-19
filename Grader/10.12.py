n = int(input())
u = set()
v = set()

for i in range(n):
    s = set(input().split())
    if i == 0:
        u = s
        v = s
    else:
        u = u.union(s)
        v = v.intersection(s)
print(len(u))
print(len(v))

