sol = input()
ans = input()
if len(sol) != len(ans):
    print("Incomplete answer")
else:
    score = 0
    for i in range(0,len(sol)):
        if sol[i]==ans[i]:
            score = score+1
    print(score)