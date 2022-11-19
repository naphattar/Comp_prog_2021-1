sentence = []
alphabet ="abcdefghijklmnopqrstuvwxyz"
bigalphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    word = input().strip()
    if word !="end":
        sentence.append(word)
    else:
        break
def rot(x):
    new = ""
    for i in range(len(x)):
        if x[i] in alphabet:
            x_pos = alphabet.index(x[i])
            new_x_pos = (x_pos+13)%26
            new = new+ alphabet[new_x_pos]
        elif x[i] in bigalphabet:
            x_pos = bigalphabet.index(x[i])
            new_x_pos = (x_pos+13)%26
            new = new+ bigalphabet[new_x_pos]

        else:
            new = new + x[i]
    return new
for i in sentence:
    print(rot(i))

          