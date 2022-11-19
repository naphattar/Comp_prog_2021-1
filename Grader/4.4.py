word = input()
result = ""
for i in range(len(word)):
    if word[i] == "(":
        result += "["
    elif word[i] == "[":
        result += "("
    elif word[i] == ")":
        result += "]"
    elif word[i] == "]":
        result += ")"
    else:
        result += word[i]
print(result)
    