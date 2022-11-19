word = input()
sentence = input()
newword =""
for i in range(0,len(sentence)):
    if "0" <= sentence[i] <= "9" or "a"<= sentence[i] <= "z" or "A" <= sentence[i] <="Z" or sentence[i] ==" ":
        newword = newword+sentence[i]
newword =newword.split()
count = 0
for i in range(0,len(newword)):
    if newword[i] == word:
        count = count+1
print(count)