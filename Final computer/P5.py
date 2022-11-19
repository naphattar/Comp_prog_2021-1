import numpy as np
def f1(x):
    x1 = x[1:,]
    x2 = x[0:len(x)-1,]
    r = x1/x2
    r = r- (x[1,]/x[0,])
    rzero = r[r == 0]
    if len(rzero) < len(r):
        return False
    else:
        return True
print(f1(np.array([1,2,4,8])))
def f3(x):
    n = x.shape[0]
    ind = np.arrange(n**2)
    ind = ind.reshape((n,n))
    check1 = ind[x==1]
    check0 = ind[x==0]
    