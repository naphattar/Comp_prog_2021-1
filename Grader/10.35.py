n = int(input())
data = []
for i in range(n):
    student = input().split()
    data.append(student)
data.sort()
search = set(input().split()) 
answer = []
for i in range(n):
    if set(data[i]).intersection(search) == search:
        answer.append(data[i])
if len(answer) == 0:
    print("Not Found")
else:
    for i in range(len(answer)):
        result = ""
        for j in answer[i]:
            result = result + str(j) + " "
        print(result[:-1])
