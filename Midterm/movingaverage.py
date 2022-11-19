data = input().split()
window = int(data[0])
number = []
result = []
for i in range(1,len(data)):
    number.append(float(data[i]))

if window > len(number):
    window = len(number)
for i in range(0,len(number)-window+1):
    s =sum(number[i:i+window])
    s = s/window
    result.append(s)
window = window -1
while window > 0:
    s = sum(number[len(number)-window:])
    s = s/window
    result.append(s)
    window = window -1
finalresult =""
for i in range(len(result)):
    finalresult = finalresult +" "+  str(result[i])
print(finalresult[1:])