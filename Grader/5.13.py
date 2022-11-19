N = int(input())
result = []
Proto = []
for i in range(N):
    if i%2 ==0:
       a = int(input())
       result.append(a)
    else:
       a = int(input())
       result.insert(0,a)
b = input()
b = b.split()
for i in range(len(b)):
    if (i+1+N)%2 == 0:
        result.insert(0,int(b[i]))
    else:
        result.append(int(b[i]))
while True:
    c = int(input())
    if c == -1:
        break
    else:
        Proto.append(c)
for i in range(len(Proto)):
    if (i+1+len(b)+N)%2 ==0:
        result.insert(0,Proto[i])
    else:
        result.append(Proto[i])
print(result)
        
    

