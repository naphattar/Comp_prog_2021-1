data = [['A102', 30], ['A103', 40], ['B014', 50], ['B109', 50]]
a,b = input().split(",")
id,score =[],[]
newid,newscore =[],[]
newdata =[]
for i in range(len(data)):
    id.append(data[i][0])
    score.append(int(data[i][1]))
a =int(a)
b =int(b)
for i in range(len(score)):
    if a<= score[i] and score[i] <=b:
        pass
    else:
        newid.append(id[i])
        newscore.append(score[i])
for i in range(len(newid)):
    newdata.append([newid[i],newscore[i]])
print(newdata)