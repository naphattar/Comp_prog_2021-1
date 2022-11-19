def factor(n): 
    result = []
    m = 2
    while m <= n:
        if n%m == 0:
            e = 0
            while n%m == 0:
                n = n/m
                e = e+1
            result.append([m,e])
        m = m+1
    return result

exec(input().strip())