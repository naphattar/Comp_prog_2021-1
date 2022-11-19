#โปรเเกรมนับจำนวนเฉพาะ
def prime(a):
    if a==1:
        return 0 
    if a==2 :
        return 1
    else:
        for i in range(2,a):
            if a%i == 0:
                return 0 
                break
            else :
                if i == a-1:
                    return 1
count = 0
c= input("ใส่เลขจุดเริ่มต้น:")
b = input("ใส่เลขจุดสิ้นสุด:")

b = int(b)
c = int(c)
for i in range(c,b+1):
    if prime(i)==1:
        print(i)
        count = count +1
if count == 0:
    print("There is no prime number")
if count == 1:
    print("There is one prime number")
else:
    print("There are "+str(count)+" prime numbers in the range "+"("+str(c)+","+str(b)+")")


    