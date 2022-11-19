N = int(input())
name = []
result = []
Fullname = ["Robert","William","James","John","Margaret","Edward","Sarah","Andrew","Anthony","Deborah"]
Nickname = ["Dick","Bill","Jim","Jack","Peggy","Ed","Sally","Andy","Tony","Debbie"]
for i in range(N):
    a = input()
    name.append(a)
for i in range(len(name)):
    if name[i] in Fullname:
        j = Fullname.index(name[i])
        print(Nickname[j])
    elif name[i] in Nickname:
        j = Nickname.index(name[i])
        print(Fullname[j])
    else:
        print("Not found")

    