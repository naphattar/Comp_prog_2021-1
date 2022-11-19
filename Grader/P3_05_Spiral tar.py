import numpy as np
def spiral_square(n):
    result = np.zeros((n,n),int)
    m = (n-1)//2 
    result[m,m] += 1
    for i in range(1,n,2):
        for j in range(i):
            result[m+(i-1)//2-j,m+(i-1)//2+1] += i**2+j+1
        for j in range(i+2):
            result[m+(i-1)//2-i,m+(i-1)//2+1-j] += i**2+i+j+1
        for j in range(i):
            result[m+(i-1)//2-i+j+1,m+(i-1)//2-i] += i**2+i+i+2+j+1
        for j in range(i+2):
            result[m+(i-1)//2+1,m+(i-1)//2-i+j] += i**2+i+i+2+i+j+1
    return result.tolist()
     # n is a positive odd number
def print_square(S):
 # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
 for i in range(len(S)):
    print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())