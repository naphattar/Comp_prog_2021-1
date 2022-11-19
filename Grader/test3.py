import numpy as np
a = np.array([1,2,3])
b = np.array([[1,3,3],[4,4,6],[4,8,9]])
n = a-b
m = n[n==0]
print(a.shape)