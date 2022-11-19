number = input().split()
number1 = number[0]
number2 = number[1]
number1 = int(number1,2)
number2 = int(number2,2)
sum = number1+number2
sum = bin(sum)
print(sum[2:])