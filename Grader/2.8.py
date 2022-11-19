import math
a = input()
a = a.split(",")
b = len(a[1])
c = a[0]+a[1]
c = int(c)
d =len(a[2])
e = (10**(d)-1)*(10**(b))
c = c*(10**d-1) + int(a[2])
g = math.gcd(c,e)
c = int(c/g)
e = int(e/g)
print(c,"/",e)


