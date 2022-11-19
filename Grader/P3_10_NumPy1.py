import numpy as np
def eq(A, B, p):
    dif = A-B
    dif = dif[dif == 0]
    m = len(dif)
    ni = np.ones(A.shape)
    n = np.sum(ni)
    if (m)/n*100 >= p:
        return True
    else:
        return False
 
def closest_point_indexes(points, p):
    distance = (points - p)**2
    dis = np.array(np.sum(distance,axis = 1))
    minimum = np.min(dis)
    result = points[dis == minimum]
    ans = []
    for i in range(len(np.sum(distance,axis = 1))):
        if dis[i] == minimum:
            ans.append(i)
    return np.array(ans)

def number_of_inversions(A):
    n = A.shape[0]
    newA = np.zeros((n,n),int)
    newA = newA + A
    
    for i in range(1,n):
        newA[i,i:] = newA[i,i:] - np.array([A[i-1]])
        
    m = len(newA[newA<0])
    return m


exec(input().strip()) 