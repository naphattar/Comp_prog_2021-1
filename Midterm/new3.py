d = []
for e in range(99999, -1, -1):
    if e not in d:
        if e%2==0:
            d.append(e)
        else:
            d.insert(0,e)
print(d[:2])