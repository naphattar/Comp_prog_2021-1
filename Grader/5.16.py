n = int(input())
seq = [n]
result = " "
while n != 1:
    if n%2 ==0:
        n = int(n/2)
        seq.append(n)
    else:
        n = 3*n+1
        seq.append(n)
if len(seq) <= 15:
    final = seq
else:
    final = seq[-15:]
for i in final:
    result = result+str(i)+"->"
print(result[1:-2])