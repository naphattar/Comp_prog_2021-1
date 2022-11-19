m = input()
n = int(input())
length = len(m)
if n>length:
     print((n-length)*"0"+m)
else:
    print(m)