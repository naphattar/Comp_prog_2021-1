n = int(input("ใส่เลขที่คุณต้องการ:"))
r = int(input("ใส่เลขที่คุณต้องการ:"))



def fac(a):
    if a ==0:
        return 1
    else:
        return fac(a-1)* a
    


def combi(n,r):
    return fac(n) / (fac(n-r)* fac(r))
sum = 0   
for i in range(0,n+1):
    sum = sum + combi(n,i)

print(sum)