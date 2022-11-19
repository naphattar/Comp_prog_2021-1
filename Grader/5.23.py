N = int(input())
X = []
Y = []
seq = []
distance1 =[]
distance2 =[]
for i in range(N):
    seq.append(i+1)
    coordinate = input()
    coordinate = coordinate.split()
    X.append(float(coordinate[0]))
    Y.append(float(coordinate[1]))
    dis = ((float(coordinate[0]))**2 +(float(coordinate[1]))**2)**(0.5)
    distance1.append(dis)
    distance2.append(dis)
distance1.sort()
j = distance2.index(distance1[2])
print("#"+str(seq[j])+":  "+"("+str(X[j])+", "+str(Y[j])+")")


