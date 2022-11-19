word = input()
extra = ["s","x"]
character = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
character = character.split(",")
def plural(word):
    if word[-1] in extra or word[-2:]=="ch":
       return word+"es"
    if word[-1] == "y":
        if word[-2] in character:
            return word[0:-1]+"ies"
        else:
            return word+"s"
    else:
        return word+"s"
print(plural(word))