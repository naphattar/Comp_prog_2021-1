a = int(input())
b = int(input())
c = int(input())
import math
x = (-b+math.sqrt(b**2-4*a*c))/2
y = (-b-math.sqrt(b**2-4*a*c))/2
if a == 1:
    print(str(x)+" เเละ "+str(y)+" เป็นคำตอบของสมการ "+"x^2+"+str(b)+"x+"+str(c))
if b==1:
    print(str(x)+" เเละ "+str(y)+" เป็นคำตอบของสมการ "+str(a)+"x^2+x+"+str(c))
else:
    print(str(x)+" เเละ "+str(y)+" เป็นคำตอบของสมการ "+str(a)+"x^2+"+str(b)+"x+"+str(c))


    