a = input().split()
b = input().split()
card = "A K Q J 10 9 8 7 6 5 4 3 2".split()
for i in range(len(a)):
    a[i] = card.index(a[i])
for i in range(len(b)):
    b[i] = card.index(b[i])
a.sort()
b.sort()
j = 0
while j<len(a):
    if a[j]<b[j]:
        print("A win")
        break
    elif b[j]<a[j]:
        print("B win")
        break
    else:
        j +=1
        if j == len(a):
            print("Draw")

    
