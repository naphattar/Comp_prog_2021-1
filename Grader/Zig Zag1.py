index = int(input())
number = input()
a =0
first =[]
second =[]
while a< index:
    number = number.split()
    first.append(int(number[0]))
    second.append(int(number[1]))
    number = input()
    a =a+1
number = input()   
k = len(first)
if number == "Zig-Zag":
    minimum = first[0]
    i,j =0,1
    while i%2 ==0 and i<k:
        minimum =min(minimum,first[i])
        i = i+2
    while j%2 !=0 and j<k:
        minimum = min(minimum,second[j])
        j = j+2
    maximum = second[0]
    m,n =0,1
    while m%2==0 and m<k:
        maximum = max(maximum,second[m])
        m = m+2
    while n%2 !=0 and n<k:
        maximum = max(maximum,first[n])
        n = n+2
if number == "Zag-Zig":
    maximum = first[0]
    i,j =0,1
    while i%2 ==0 and i<k:
        maximum =max(maximum,first[i])
        i = i+2
    while j%2 !=0 and j<k:
        maximum = max(maximum,second[j])
        j = j+2
    minimum = second[0]
    m,n =0,1
    while m%2==0 and m<k:
        minimum = min(minimum,second[m])
        m = m+2
    while n%2 !=0 and n<k:
        minimum = min(minimum,first[n])
        n = n+2
print(minimum,maximum)       


