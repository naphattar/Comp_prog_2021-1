import math
number = input().split(",")

integer = int(number[0])

down = int("9"*len(number[2]))+"0"*len(number[1])

up = int(number[0]+number[1]+number[2])-int(number[0]+number[1])

gcd = math.gcd(down,up)

print(str(up//gcd),"/",str(down//gcd))