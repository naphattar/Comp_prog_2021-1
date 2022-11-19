import math
a = float(input())
b = float(input())
t = 0.6157-0.0188*((math.log(a))/math.log(10))
m = (math.sqrt(a*b))/60
h = 0.024265*(a**(0.5378))*(b**(0.3964))
y = 0.0333*(a**(t))*(b**(0.3))
print(m)
print(h)
print(y)