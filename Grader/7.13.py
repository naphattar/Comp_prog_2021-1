word = input()
wordlist = []
def remove(n):
    output = ""
    for ch in n:
        if ch in "\'\"\\()[];:.,><=":
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
        if i ==0:
            wordlist[i] = wordlist[i].lower()
        else:
            wordlist[i] = wordlist[i].lower()
            if len(wordlist[i]) ==1:
                wordlist[i] = wordlist[i].upper()
            else:
                wordlist[i] = wordlist[i][0].upper()+wordlist[i][1:]
    for word in wordlist:
        output += word
    return output
print(camel(word))           

    
    


   
#"\'\"\\()[];:.,"
