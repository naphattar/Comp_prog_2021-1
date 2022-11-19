import numpy as np
# A is a 2-d array
def get_column_from_bottom_to_top( A, c ):
    return A[::-1,c]



def get_odd_rows( A ):
    return A[1::2,::]


def get_even_column_last_row( A ):
    return A[-1,0::2]

def get_diagonal1( A ): 
    shape = []
    for i in range(A.shape[0]):
        shape.append(i)
    return A[shape,shape]
    # A is a square matrix
 # from top-left corner down to bottom-right corner
def get_diagonal2( A ):
    shape = []
    shape2 = []
    for i in range(A.shape[0]-1,-1,-1):
        shape.append(i)
        shape2.append(i)
    shape.sort()
    return A[shape,shape2]
    
     # A is a square matrix
 # from top-right corner down to bottom-left corner
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ