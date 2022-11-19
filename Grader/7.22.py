word1 = input()
word2 = input()
def remove(n):
    output = ""
    for ch in n:
        if ch in "\'\"\\)([];:.,><=":
            output +=" "
        elif ch in "-_":
            output +=""
        else:
            output += ch
    return output
def camel(n):
    n = remove(n)
    output = ""
    wordlist = n.split()
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].lower()       
    for word in wordlist:
        output += word
    return output
word1 = camel(word1)
word2 = camel(word2)
wordlist1,wordlist2 = [],[]
for i in word1:
    wordlist1.append(i)
for i in word2:
    wordlist2.append(i)
wordlist1.sort()
wordlist2.sort()
if wordlist2 == wordlist1:
    print("YES")
else:
    print("NO")
