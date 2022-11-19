def row_number(t, e):
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == e:
                return i

def flatten(t):
    result = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] != 0:
                result.append(t[i][j])
    return result
def inversions(x):
    count = 0
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i] > x[j]:
                count = count +1
    return count
def solvable(t):
    if (len(t))%2 == 0:
        if (inversions(flatten(t)))%2 == 0:
            if row_number(t,0) %2 != 0:
                return True
            else:
                return False
        else:
            if row_number(t,0) %2 == 0:
                return True
            else:
                return False
    else:
        if (inversions(flatten(t)))%2 == 0:
            return True
        else:
            return False


exec(input().strip())