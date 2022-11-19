first = input()
second = input()
first = first.split()
second = second.split()
date1 = first[2]
date2 = second[2]
date1 =date1[:-1]
date2 = date2[:-1]
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
month1 = month.index(first[1])
month2 = month.index(second[1])
if int(first[3])<int(second[3]):
    result = first[0]
elif int(first[3])>int(second[3]):
    result = second[0]
else:
    if month1<month2:
        result = first[0]
    elif month1>month2:
        result = second[0]
    else:
        if int(date1)<int(date2):
            result = first[0]
        elif int(date1)>int(date2):
            result = second[0]
        else:
            result = first[0]+" "+second[0]
print(result)
        


