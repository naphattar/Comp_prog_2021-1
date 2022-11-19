n = int(input())
icecream = {}
icecreamlist,icesoldlist,amountlist=[],[],[]
for i in range(n):
    ice,price = input().split()
    icecream[ice] = float(price)
    icecreamlist.append(ice)
m = int(input())
sold = {}
for i in range(m):
    ice,amount= input().split()
    sold[ice] = float(amount)
    icesoldlist.append(ice)
    amountlist.append(float(amount))
totalsold = {}
for i in range(m):
    sumprice = 0
    for j in range(m):
        if icesoldlist[j] == icesoldlist[i]:
            sumprice = sumprice + amountlist[j]
    totalsold[icesoldlist[i]] =  sumprice
income = 0
totalprice = []
for ice in totalsold:
    if ice in icecreamlist:
        income = income + totalsold[ice]*icecream[ice]
        totalprice.append(totalsold[ice]*icecream[ice])   
if income > 0:
    print("Total ice cream sales:",income)
    maxprice = max(totalprice)
    topsale = []
    for ice in totalsold:
        if ice in icecreamlist and totalsold[ice]*icecream[ice] == maxprice:
            topsale.append(ice)
    topsale.sort()
    topsaleice = ""
    for i in topsale:
        topsaleice += i+", "
    print("Top sales: "+topsaleice[:-2])
else:
    print("No ice cream sales")
