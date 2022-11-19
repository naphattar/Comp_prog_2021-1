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
    print(ids[i],grade[i])
        
        
    