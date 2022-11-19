def flip(x):
    xlist = []
    new =""
    for i in range(len(x)):
        xlist.append(x[i])
    for i in range(len(x)-1,-1,-1):
        new += xlist[i]
    return new
print(flip("tarrtartar"))