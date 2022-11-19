day = int(input())
month = int(input())
year =int(input())
year = year-543
if year%4==0 and year%100!=0:
    if month ==1:
        print(day)
    elif month ==2:
        print(day+31)
    elif month ==3:
        print(day+60)
    elif month ==4:
        print(day+90+1)
    elif month ==5:
        print(day+120+1)
    elif month ==6:
        print(day+151+1)
    elif month ==7:
        print(day+181+1)
    elif month ==8:
        print(day+212+1)
    elif month ==9:
        print(day+243+1)
    elif month ==10:
        print(day+273+1)
    elif month ==11:
        print(day+304+1)
    elif month ==12:
        print(day+334+1)
if year%400 ==0:
    if month ==1:
        print(day)
    elif month ==2:
        print(day+31)
    elif month ==3:
        print(day+60)
    elif month ==4:
        print(day+90+1)
    elif month ==5:
        print(day+120+1)
    elif month ==6:
        print(day+151+1)
    elif month ==7:
        print(day+181+1)
    elif month ==8:
        print(day+212+1)
    elif month ==9:
        print(day+243+1)
    elif month ==10:
        print(day+273+1)
    elif month ==11:
        print(day+304+1)
    elif month ==12:
        print(day+334+1)
else:
    if month ==1:
        print(day)
    elif month ==2:
        print(day+31)
    elif month ==3:
        print(day+59)
    elif month ==4:
        print(day+90)
    elif month ==5:
        print(day+120)
    elif month ==6:
        print(day+151)
    elif month ==7:
        print(day+181)
    elif month ==8:
        print(day+212)
    elif month ==9:
        print(day+243)
    elif month ==10:
        print(day+273)
    elif month ==11:
        print(day+304)
    elif month ==12:
        print(day+334)
