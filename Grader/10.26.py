n = int(input())
Data,City = [],[]
for i in range(n):
    ID,city = input().split(":")
    city = set(city.split(","))
    Data.append(ID)
    City.append(city)
search = input()
sub = Data.index(search)
searchset = City[sub]
answer = []
for i in range(len(Data)):
    if i!= sub and len(searchset.intersection(City[i]))>0:
        answer.append(Data[i])
if len(answer) == 0:
    print("Not Found")
else:
    for i in answer:
        print(i)
    