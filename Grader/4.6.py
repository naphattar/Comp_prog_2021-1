h = int(input())
if h>2:
    print((h-1)*" "+"*"+(h-1)*" ")
    for i in range(2,h):
        print((h-i)*" " +"*"+(2*i-3)*" "+"*")
    print((2*h-1)*"*")
if h ==2:
    print(" "+"*"+" ")
    print(3*"*")