import numpy as np
def leap(years):
    years = years - 543
    if years%4 == 0:
        if years%100 ==0:
            if years%400 ==0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
print(leap(np.array([2543,2559,2560])))