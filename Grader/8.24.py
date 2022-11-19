text = {"0":" "}
alphabet = "abcdefghijklmnopqrstuvwxyz "
k = 0
for i in range(2,10):
    if i == 9 or i ==7:
        i = str(i)
        for j in range(4):
            text[i*(j+1)] = alphabet[k]
            k = k+1
    else:
        i = str(i)
        for j in range(3):
            text[i*(j+1)] = alphabet[k]
            k = k+1
def reverse(d):
    key,value = [],[]
    newd = {}
    for k in d:
        key.append(k)
        value.append(d[k])
    for i in range(len(key)):
        newd[value[i]] = key[i]
    return newd
number = reverse(text)
def text2keys( sen ):
    result = ""
    sen = sen.lower()
    for i in sen:
        if i in alphabet:
            result = result + number[i]+" "
    return result[:-1]
def keys2text( keys ):
    keys = keys.split()
    result = ""
    for i in keys:
        if i in text:
            result = result + text[i] 
    return result

exec(input().strip())





