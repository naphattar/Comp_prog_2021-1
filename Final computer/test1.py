import numpy as np
def f1(x): # x เป็น 1-D numpy array of floats
    n = len(x)
    p = np.ndarray((n,n))
    for r in range(n):
        for c in range(n):
            p[r,c] = x[r]+x[c]
    return p
print(f1([1,2,6,8]))
def f2(x):
    a = (x.reshape(1,len(x))).T
    return x+a
print(f2(np.array([1,2,6,8])))