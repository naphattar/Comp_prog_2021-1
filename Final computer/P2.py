n = int(input())
car = {}
number = {}
for i in range(n):
    order = input().split()
    name = order[0]+" "+order[1]
    brand = order[2]
    num = order[3]
    if name in car:
        car[name] = car[name]+[[brand,num]]
    else:
        car[name] = [[brand,num]]
    if num in number:
        number[num] = number[num]+[name]
        number[num] = set(number[num])
        number[num] = list(number[num])
        number[num].sort()
    else:
        number[num] = [name]
        number[num] = set(number[num])
        number[num] = list(number[num])
        number[num].sort()
def search(ord): 
    ans = ""
    if ord in car:
        allcar = car[ord]
        for i in range(len(allcar)):
            ans = ans +str(allcar[i][0])+ " "+str(allcar[i][1])+", "
        print( ord+" --> "+ans[:-2])
    elif ord in number:
        allname = number[ord]
        ans = ""
        ans = ans + ", ".join(allname)
        print( ord+" --> "+ans)
        
    else:
        print(ord+" --> "+"Not Found")
print(car)


m = int(input().strip())
for i in range(m):
    search(input())