k = int(input())
domino = input()
k = k-1
x,y = domino[5*k+1:5*k+4].split(":")
newdo1 = domino[0:5*k+1]
newdo2 = domino[5*k+4:]
newdo3 = str(y)+":"+str(x)
print(newdo1+newdo3+newdo2)
