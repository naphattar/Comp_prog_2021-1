import numpy as np
def peak_indexes(x):
   x1 = x[1:-1:]
   pos = np.arange(x1.shape[0])
   xleft = x[:-2:]
   xright = x[2::]
   d1 = x1-xleft
   d2 = x1-xright
   peak = pos[(d1>0)&(d2>0)]
   return peak+1
 
 
def main():
 d = np.array([float(e) for e in input().split()])
 pos = peak_indexes(np.array(d))
 if len(pos) > 0:
    print(", ".join([str(e) for e in pos]))
 else:
    print("No peaks")
exec(input().strip()) # Don't remove this line