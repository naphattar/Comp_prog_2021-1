day = int(input())
month = int(input())
year = int(input())- 543

def leap(years):
    if years%4 == 0:
        if years%100 ==0:
            if years%400 ==0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

komyear = [1,3,5,7,8,10,12]
tar = {}
for i in range(13):
    if i == 0:
        tar[i] = 0
    elif i in komyear:
        tar[i] = 31
    elif i != 2:
        tar[i] = 30
    else:
        tar[i] = 28+ leap(year)


result = 0
for i in range(month):
    result = result+tar[i]
result = result+day

print(result)
        


