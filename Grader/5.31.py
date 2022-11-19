card = input()
card = card.split()
seq = input()
st = ((len(card))//2)
for i in range(len(seq)):
    if seq[i] == "C":
        card = card[st:]+card[0:st]
    if seq[i] == "S":
        half = card[st:]
        newcard = []
        for j in range(0,st):
            newcard.append(card[j])
            newcard.append(half[j])
        card = newcard
    else:
        pass
result = card[0]
for i in range(1,len(card)):
    result = result +" "+card[i]
print(result)  

        
        
