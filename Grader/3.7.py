a =int(input())
if a<1000:
    print(a)
elif 999<a<10000:
    b = (a//1000)
    c = str(a-b*1000)
    if int(c[1])> 4:
        if int(c[0])==9:
            b = b+1
            print(str(b)+"K")
        else :
            d=int(c[0])+1
            print(str(b)+"."+str(d)+"K")
    else:
        e = (a-b)//100
        print(str(b)+"."+str(e)+"K")
elif 9999<a<1000000:
    b =(a//1000)
    c =str(a-b*1000)
    if int(c[0])>4:
        b =b+1
    print(str(b)+"K")    
elif 999999<a<10000000:
    b = (a//1000000)
    c =str(a-b*1000000)
    if int(c[1])> 4:
        if int(c[0])==9:
            b = b+1
            print(str(b)+"M")
        else :
            d=int(c[0])+1
            print(str(b)+"."+str(d)+"M")
    else:
        e = (a-b)//100
        print(str(b)+"."+str(e)+"M")
elif 9999999<a<1000000000:
    b =(a//1000000)
    c =str(a-b*1000000)
    if int(c[0])>4:
        b =b+1
    print(str(b)+"M")    
elif 999999999<a<10000000000:
    b = (a//1000000000)
    c =str(a-b*1000000000)
    if int(c[1])> 4:
        if int(c[0])==9:
            b = b+1
            print(str(b)+"B")
        else :
            d=int(c[0])+1
            print(str(b)+"."+str(d)+"B")
    else:
        e = (a-b)//100
        print(str(b)+"."+str(e)+"B")
else:
    b =(a//1000000000)
    c =str(a-b*1000000000)
    if int(c[0])>4:
        b =b+1
    print(str(b)+"B") 


