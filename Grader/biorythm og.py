import math
pi = math.pi
bd,bm,by,d,m,y = [int(e) for e in input().split()]
y = y-543
by = by-543
count = 0

def seq(day,month,year):
    if year%4 !=0:
        if month ==1:
           return(day)
        elif month ==2:
           return(day+31)
        elif month ==3:
           return(day+59)
        elif month ==4:
           return(day+90)
        elif month ==5:
           return(day+120)
        elif month ==6:
           return(day+151)
        elif month ==7:
           return(day+181)
        elif month ==8:
           return(day+212)
        elif month ==9:
           return(day+243)
        elif month ==10:
           return(day+273)
        elif month ==11:
           return(day+304)
        elif month ==12:
           return(day+334)
    if year%4 ==0:
        if month ==1:
           return(day)
        elif month ==2:
           return(day+31)
        elif month ==3:
           return(day+60)
        elif month ==4:
           return(day+91)
        elif month ==5:
           return(day+121)
        elif month ==6:
           return(day+152)
        elif month ==7:
           return(day+182)
        elif month ==8:
           return(day+213)
        elif month ==9:
           return(day+244)
        elif month ==10:
           return(day+274)
        elif month ==11:
           return(day+305)
        elif month ==12:
           return(day+335)
if by%4 ==0:
    diff1 = 367-seq(bd,bm,by)
else:
    diff1 = 366-seq(bd,bm,by)
diff3 = seq(d,m,y)-1
diff2 = 365*(y-by-1)+count
t = diff1+diff2+diff3
physical = math.sin(2*pi*t/23)
emo = math.sin(2*pi*t/28)
intel = math.sin(2*pi*t/33)

print(t,"{:.2f}".format(physical),"{:.2f}".format(emo),"{:.2f}".format(intel))