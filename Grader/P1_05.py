par,stroke,choice,realstroke= [] , [] , [] ,[]
for i in range(9):
    g = input().split()
    par.append(float(g[0]))
    stroke.append(float(g[1]))
    choice.append(float(g[2]))
    if float(g[2]) == 1:
        realstroke.append(min(stroke[i],par[i]+2))
sumrealstroke = sum(realstroke)
sumpar = sum(par)
a = 1.5*sumrealstroke - sumpar
a = 0.8*a
if a >= 0:
    tamtor = int(a)
else:
    tamtor = int(a)-1
totalscore = sum(stroke)-tamtor
print(int(sum(stroke)))
print(tamtor)
print(int(totalscore))




