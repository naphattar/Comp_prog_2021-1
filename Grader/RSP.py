rsp = input()
rsp.split()
score1,score2 = 0,0
if rsp[0] =="R" and rsp[1] =="S":
    score1 +=1
elif rsp[0] =="R" and rsp[1] =="P":
    score2 +=1
elif rsp[0] =="S" and rsp[1] =="P":
    score1 +=1
elif rsp[0] =="S" and rsp[1] =="R":
    score2 +=1
elif rsp[0] =="P" and rsp[1] =="S":
    score2 +=1
elif rsp[0] =="P" and rsp[1] =="R":
    score1 +=1
else:
    pass

