alpha = "A23456789TJQK"
alphadok = "CDHS"
card = {}
dok = {}
for i in range(13):
    card[alpha[i]] = i+1
for i in range(4):
    dok[alphadok[i]] =i+1


cards = input()
cardlist = []
for i in range(0,len(cards),2):
    cardlist.append(cards[i:i+2])
def good(x):
    if x> 0:
        return "+"+str(x)
    else:
        return str(x)
def dis(x,y):
    if card[x[0]]-card[y[0]] == 0:
        return good(dok[x[1]]-dok[y[1]])
    else:
        return good(card[x[0]]-card[y[0]])
result =""
for i in range(0,len(cardlist)-1):
    result = result + str(dis(cardlist[i],cardlist[i+1]))
print(result)



