import numpy as np
def f1(x, a): 
    # x เป็น 1-D numpy array of ints, a เป็น int
    m = x[0]
    for e in x[1:]:
        if e > m: 
            m = e
    for i in range(len(x)):
        if x[i] == m: 
            x[i] = a
    return x
print(f1(np.array([3,4,9,67,98]),100))
def f2(x, a):
    x[x == np.max(x)] = a
    return x
print(f2(np.array([3,4,9,67,98]),100))
