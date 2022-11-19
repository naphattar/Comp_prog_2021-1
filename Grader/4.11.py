sentence = input()
start,i = 0,0
number = []
remark = []
while i<len(sentence):
    if start > len(sentence):
        break
    if i> len(sentence)-1:
        break
    while sentence[start] == sentence[i]:
        i = i+1
        if i == len(sentence):
            break
    number.append(i-start)
    remark.append(sentence[start])
    start =i    
#print(number,remark)
output = remark[0]+" "+str(number[0] )
for j in range(1,len(number)):
    output = output+" "+ remark[j]+" "+str(number[j])
print(output)


    
    
    