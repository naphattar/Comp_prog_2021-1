n = int(input())
telephone = {}
for i in range(n):
    name,surname,tel = input().split()
    telephone[name+" "+surname] = tel
def reverse(d):
    key,value = [],[]
    newd = {}
    for k in d:
        key.append(k)
        value.append(d[k])
    for i in range(len(key)):
        newd[value[i]] = key[i]
    return newd
namete = reverse(telephone)
result = []
m = int(input())
for i in range(m):
    sea = input()
    if sea in telephone:
        result.append(sea+" --> "+telephone[sea])
    elif sea in namete:
        result.append(sea+" --> "+namete[sea])
    else:
        result.append(sea+" --> Not found")
for i in result:
    print(i)
    

