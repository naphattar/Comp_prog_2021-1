result = input().strip()
target = int(input())
new = ""
frame = []
for i in range(len(result)):
    if result[i] =="X":
        new = new + result[i] + "t"
    else:
        new = new + result[i]
for i in range(0,18,2):
    frame.append(new[i:i+2])
frame.append(new[18:])
for i in range(10):
    if "Xt" in frame[i]:
        frame[i] =frame[i].replace("Xt","X")
scoref,realscore = [],[]
for i in range(9):
    if frame[i] =="X":
        scoref.append([frame[i]])
        realscore.append([10])
    elif frame[i][1] =="/":
        realscore.append([int(frame[i][0]),10-int(frame[i][0])])
    else:
        scoref.append([frame[i][0],frame[i][1]])
        realscore.append([int(frame[i][0]),int(frame[i][1])])
if len(frame[9]) == 3:
    scoref.append([frame[9][0],frame[9][1],frame[9][2]])
    if frame[9][0] =="X":
        if frame[9][1] =="X":
            if frame[9][2] =="X":
                realscore.append([10,10,10])
            else:
                realscore.append([10,10,int(frame[9][2])])
        else:
            if frame[9][2] =="/":
                realscore.append([10,int(frame[9][1]),10-int(frame[9][1])])
            else:
                realscore.append([10,int(frame[9][1]),int(frame[9][2])])
    else:
        if frame[9][2] =="X":
            realscore.append([int(frame[9][0]),10-int(frame[9][0]),10])
        elif frame[9][1] =="/":
            realscore.append([int(frame[9][0]),10-int(frame[9][0]),int(frame[9][2])])
        else:
            realscore.append([int(frame[9][0]),10-int(frame[9][1]),int(frame[9][2])])
    
else:
    scoref.append([frame[9][0],frame[9][1]])
    if frame[9][1] =="/":
        realscore.append([int(frame[9][0],10-int(frame[9][0]))])
    else:
        realscore.append([int(frame[9][0]),int(frame[9][1])])
score = []
for i in range(8):
    if frame[i] =="X":
        if len(realscore[i+1]) >= 2:
            score.append(10+realscore[i+1][0]+realscore[i+1][1])
        elif len(realscore[i+1])==1:
            score.append(10+realscore[i+1][0]+realscore[i+2][0])
    elif frame[i][1] == "/":
        score.append(realscore[i][0]+realscore[i][1]+realscore[i+1][0])
    else:
        score.append(realscore[i][0]+realscore[i][1])
if frame[8] =="X":
    score.append(10+realscore[9][0]+realscore[9][1])
elif frame[8][1] =="/":
    score.append(realscore[8][0]+realscore[8][1]+realscore[9][0])
else:
    score.append(realscore[8][0]+realscore[8][1])
score.append(sum(realscore[9]))
if 1<= target <= 10:
    print(score[target-1])
else:
    print(sum(score))

    