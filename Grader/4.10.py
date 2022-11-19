a = float(input())
b = a
U = 1
while a//10 > 0 :
    a = a//10
    U = U+1
print(U)
L = 0
x = (L+U)/2
while abs(b-10**x) > ((10)**(-10))*max(b,10**x):
    if 10**x > b:
        U =x
    
    if 10**x <b:
        L =x
    x =(L+U)/2
print(round(x,6))        

