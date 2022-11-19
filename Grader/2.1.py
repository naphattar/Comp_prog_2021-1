number = input()
b = 0
for i in range(0,12):
    b = b+(13-i)*int(number[i])
    b = b%11
b = (11-b)%10
print(number[0],number[1:5],number[5:10],number[10:12],b)
