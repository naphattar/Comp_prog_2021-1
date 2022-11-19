import numpy as np
def convex_polygon_area(p):
    n = len(p)
    sum1,sum2 = 0,0
    for i in range(n-1):
        sum1 = sum1+ p[i][0]*p[i+1][1]
    sum1 = sum1+p[n-1][0]*p[0][1]
    for i in range(n-1):
        sum2 = sum2+ p[i][1]*p[i+1][0]
    sum2 = sum2+p[n-1][1]*p[0][0]
    return 0.5*(abs(sum1-sum2))


def is_heterogram(s):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    word = s.lower()
    ans = 0
    alpha = {}
    for i in range(26):
        alpha[alphabet[i]] = 0
    for i in word:
        if i in alphabet:
            alpha[i] = alpha[i]+1
    for i in word:
        if i in alphabet:
            if alpha[i] > 1:
                ans = ans+1
    if ans >0 :
        return False
    else:
        return True
    
def replace_ignorecase(s, a, b):
    news = s
    
    n = len(a)
    i = 0
    while i<= len(news)-n:
        check = (news[i:i+n]).lower()
        if check == a.lower():
            news = news[:i]+b+news[i+n:]
            i = i+len(b)
        else:
            i = i+1
    return news

def reverse_sort(x):
    x.sort()
    ret = []
    for i in range(len(x)-1,-1,-1):
        ret.append(x[i])
    return ret


def top3(votes):
    result = []
    val = votes.values()
    vallist = list(val)
    keyy = votes.keys()
    keylist = list(keyy)
    valset = set(vallist)
    vallistt = list(valset)
    newval = reverse_sort(vallistt)
    
    newkey = sorted(keylist)
    for i in range(len(newval)):
        for j in range(len(newkey)):
            if votes[newkey[j]] == newval[i]:
                if len(result) == 3:
                    break
                else:
                    result.append(newkey[j])
                    
                

    return result

# ตอ้ งมคี ำสั่งข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ
for k in range(2):
 exec(input().strip())