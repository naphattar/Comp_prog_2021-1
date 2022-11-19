data = input()
data = data.split()
peak = 0
for i in range(len(data)):
    data[i] = float(data[i])
if len(data) < 3:
    print(0)
else:
    for i in range(1,len(data)-1):
        if data[i-1]<data[i] and data[i+1]<data[i]:
            peak = peak+1
print(peak)