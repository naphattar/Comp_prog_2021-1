n = int(input())
if n>0:
    print("positive")
    if n%2 == 0:
        print("even")
    else:
        print("odd")
if n<0:
    print("negative")
    if n%2 == 0:
        print("even")
    else:
        print("odd")
if n==0:
    print("zero")
    print("even")
