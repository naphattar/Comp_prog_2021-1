i = input()
a =i[3]+i[10]+i[17]+i[24]+i[31]
b =i[7]+i[12]+i[17]+i[22]+i[27]
a = int(a)
b = int(b)
c = a+b+10000
c = c//10
c = c%1000
c = str(c)
d = int(c[0])+int(c[1])+int(c[2])
d =(d%10)+1
e ="ABCDEFGHIJ"
print(c+e[d-1])
#99999999999999999999999999999999