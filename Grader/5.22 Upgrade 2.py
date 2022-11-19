ids = []
grade = []
stu = []
while True:
    score = input()  
    if score == "q":
        break  
    score = score.split()
    ids.append(score[0])
    grade.append(score[1])
special = input()
special = special.split()
for i in special:
    stu.append(i)

point = ["F","D","D+","C","C+","B","B+","A"]
for i in range(len(stu)):
    if stu[i] in ids:
        j = ids.index(stu[i])
        if grade[j] == "A":
            grade[j] == "A"
        else:
            k = point.index(grade[j])
            grade[j] = point[k+1]
for i in range(len(ids)):
    ids[i] = int(ids[i])

newids = []
for i in ids:
    newids.append(i)
newgrade = []
newids.sort()
for i in range(len(newids)):
    j = ids.index(newids[i])
    newgrade.append(grade[j])
for i in range(len(newids)):
    print(newids[i],newgrade[i])

