order = input().strip()
n = int(input().strip())
wordlist = []
newword = []
error =[]
def flip(x):
    xlist = []
    new =""
    for i in range(len(x)):
        xlist.append(x[i])
    for i in range(len(x)-1,-1,-1):
        new += xlist[i]
    return new
for i in range(n):
    word = input().strip()
    wordlist.append(word)
for i in wordlist:
    if len(i) != len(wordlist[0]):
        error.append("Invalid size")
if len(error) == 0:
    m = len(wordlist[0])
    if order == "90":
        for i in range(m):
            new = ""
            for j in range(n-1,-1,-1):
                new += wordlist[j][i]
            newword.append(new)
    elif order == "flip":
        for x in wordlist:
            newword.append(flip(x))
    elif order =="180":
        for i in range(n-1,-1,-1):
            newword.append(flip(wordlist[i]))
    for i in newword:
        print(i)
else:
    print("Invalid size")

            

    