import numpy as np
n = int(input())
k = int(input())
def flip(x):
    xlist = []
    new =""
    for i in range(len(x)-1,-1,-1):
        xlist.append(x[i])
    return xlist

def gray(n):
    if n == 1:
        return ["0","1"]
    else:
        result = gray(n-1)+flip(gray(n-1))
        for i in range(2**(n-1)):
            result[i] = "0"+result[i]
        for i in range(2**(n-1),2**n):
            result[i] = "1"+result[i]
        return result

if n < 0 :
    if k<1:
        print("Invalid n and k")
    else:
        print("Invalid n")
else:
    if k<1 :
        print("Invalid k")
    else:
        out = ''
        for i in range(1,k+1):
            if i == k:
                m = n-len(str(i))
            else:
                m = n-len(str(i))+1

            out += str(i) + '-'*m
        print(out)
        m = (2**n)//k+1
        for i in range(m):
            print(",".join(gray(n)[k*i:k*i+k]))
        #print(",".join(gray(n)[m*k:]))

        

