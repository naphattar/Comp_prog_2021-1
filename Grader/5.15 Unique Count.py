number = input()
number = number.split()
for i in range(len(number)):
    number[i] = int(number[i])
number.sort()
result = [number[0]]
start = 0
for i in range (len(number)):
    
    if number[start]==number[i]:
        i = i+1
    else:
        result.append(number[i])
        start = i
print(len(result))
print(result[0:10])