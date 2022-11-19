sen = input()
number = []
k = 0
for i in range(0,10):
    number.append(str(i))
for i in range(0,10):
    i = str(i)
    if i in sen:
        k = k+1
        number.remove(i)
if k == 10:
    print("None")
else:
    result = " "
    for i in number:
        result = result + i +","
    print(result[1:-1])

