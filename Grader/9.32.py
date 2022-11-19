def first_fit(L, e):
    if len(L) == 0:
        L.append([e])
    else:
        i = 0
        while sum(L[i])+e > 100:
            i = i+1
            if i>= len(L):
                break
        if i >= len(L):
            L.append([e])
        else:
            L[i].append(e)

def best_fit(L, e):
    if len(L) == 0:
        L.append([e])
    else:
        different,realdifferent = [],[]
        for i in range(len(L)):
            if 100-sum(L[i])-e >= 0:
                different.append(100-sum(L[i])-e)
            realdifferent.append(100-sum(L[i])-e)
        if len(different) >0:
            minimum = min(different)
            pos = realdifferent.index(minimum)
            L[pos].append(e)
        else:
            L.append([e])
def partition_FF(D):
    result = []
    for i in range(len(D)):
        first_fit(result,D[i])
    return result

def partition_BF(D):
    result = []
    for i in range(len(D)):
        best_fit(result,D[i])
    return result

exec(input().strip()) 