import numpy as np
def eq(A,B,p):
    return np.sum(A==B)*100/(A.size)>=p
def closest_point_indexes(point,p):
    index=np.arange(len(point))
    distance =np.sum((point-p)**2,axis=1)**0.5
    return index[distance == min(distance)]
def number_of_inversions(A):
    count=0
    for i in range(np.shape(A)[0]):
        count+=np.sum(A[i]>A[i:])
    return count
exec(input().strip())
