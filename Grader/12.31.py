class Point:
 def __init__(self, x, y):
    self.x = x
    self.y = y
 def __str__(self):
    return "("+str(self.x)+","+str(self.y)+")"
class Rect:
 def __init__(self, p1, p2):
    self.lowerleft = p1
    self.upperright = p2
    
 def area(self):
     p1 = self.lowerleft
     p2 = self.upperright
     width = float(p2.x) - float(p1.x)
     length = float(p2.y) - float(p1.y)
     return int(width*length)
 
 def contains(self, p):
     p1 = self.lowerleft
     p2 = self.upperright
     if float(p1.x) <= float(p.x) <= float(p2.x) and float(p1.y) <= float(p.y) <= float(p2.y):
         return True
     else:
         return False

 


x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
 x,y = [int(e) for e in input().split()]
 p = Point(x,y)
 print(rect.contains(p)) 