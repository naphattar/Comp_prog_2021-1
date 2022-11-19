from unittest import result


dna = input().upper()
ope = input()
test = "ACTG"
result = ""
if ope == "R":
    for word in dna:
        if word in test:
            result += test[(test.index(word)+2)%4]
        else:
            result = "Invalid DNA"
            break
    print(result)
elif ope == "F":
    test = "ATCG"
    result = [0,0,0,0]
    for word in dna:
        if word in test:
            result[test.index(word)] += 1
        else:
            result = "Invalid DNA"
            break
    if result != "Invalid DNA":
        print("A="+str(result[0])+", T="+str(test[1])+", G="+str(test[2])+", C="+str(test[3]))
    else:
        print("Invalid DNA")
