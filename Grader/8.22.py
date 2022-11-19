n = int(input())
icecream = {}
icesold = {}
for i in range(n):
    ice,price = input().split()
    icecream[ice] = float(price)
m = int(input())
for i in range(m):
    ice,amount = input().split()
    if ice in icesold:
        icesold[ice] +=  float(amount)
    else:
        icesold[ice] = float(amount)
total = 0
icetotal = {}
maxx = 0
bestsell = []
for ice in icesold:
    if ice in icecream:
        total += icecream[ice]*icesold[ice]
        icetotal[ice] = icecream[ice]*icesold[ice]
        maxx = max(maxx,icecream[ice]*icesold[ice])
if total > 0:
    print("Total ice cream sales:",total)
    for ice in icetotal:
        if icetotal[ice] == maxx:
            bestsell.append(ice)
    bestsell.sort()
    final = ""
    for i in bestsell:
        final += i +", "
    print("Top sales: "+final[:-2])
else:
    print("No ice cream sales")





