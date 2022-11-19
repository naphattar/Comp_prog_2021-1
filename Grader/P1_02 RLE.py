typ = input()
if typ == "str2RLE":
    sentence= input()
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
    output = remark[0]+" "+str(number[0] )
    for j in range(1,len(number)):
       output = output+" "+ remark[j]+" "+str(number[j])
    print(output)
elif typ == "RLE2str":
    sentence= input()
    sentence = sentence.split()
    output =" "
    for i in range(len(sentence)-1):
        if i %2 ==0:
            output = output+(int(sentence[i+1]))*(sentence[i])
    print(output[1:])
else:
    print("Error")
            
