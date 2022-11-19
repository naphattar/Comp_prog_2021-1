m = int(input())
score1,score2 =0,0
Winner = 0
for i in range(3*m):
    rsp = input()
    rsp = rsp.split()
    if rsp[0] =="R" and rsp[1] =="S":
       score1 =score1+1
    elif rsp[0] =="R" and rsp[1] =="P":
       score2 = score2+1
    elif rsp[0] =="S" and rsp[1] =="P":
       score1 = score1+1
    elif rsp[0] =="S" and rsp[1] =="R":
       score2 = score2+1
    elif rsp[0] =="P" and rsp[1] =="S":
       score2 = score2+1
    elif rsp[0] =="P" and rsp[1] =="R":
         score1 = score1+1
    else:
         pass
    if score1 == m and score2 < m:
        Winner = "Player 1 wins"
        break
    elif score2 == m and score1 < m:
        Winner = "Player 2 wins" 
        break
    else:
        pass
if score1 == score2:
    Winner = "Tie"
print(score1,score2)
print(Winner)


    
