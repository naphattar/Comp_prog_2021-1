a = int(input("ใส่เลขตัวที่ 1:"))
#b = int(input("ใส่เลขตัวที่ 2:"))
def prime(x):
    if x==1:
        return 0
    if x==2:
        return 1
    if x==3:
        return 1
    else:
        for  i in range(2,x):
            if x%i == 0:
                return 0
            else:
                i = i+1
            if i == x-2:
                return 1
tar =[]
for j in range(1,a+1):
    if prime(j):
        tar.append(j)
print(tar)
count = len(tar)
print("ในช่วง 1 ถึง "+str(a)+" มีจำนวนเฉพาะอยู่ "+str(count)+" ตัว")
