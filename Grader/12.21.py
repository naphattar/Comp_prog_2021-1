class Complex :
 def __init__(self,a,b):
     self.a = a
     self.b = b


 def __str__(self):
     if self.a == 0:
         if self.b > 0:
            if float(self.b) == 1.0:
                return "i"
            else:
                return str(self.b)+"i"
         elif self.b == 0:
            return str(0)
         else:
             if float(self.b) == -1.0:
                 return "-i"
             elif float(self.b)-int(self.b) == 0:
                b = int(self.b)
             else:
                b = float(self.b)
             return "-"+str(-1*b)+"i"
     else:
        if float(self.b) > 0:
            if float(self.b) == 1.0:
                return str(self.a)+"+"+"i"
            else:
                return str(self.a)+"+"+str(self.b)+"i"
        elif float(self.b) == 0:
            return str(self.a)
        else:
            if float(self.b) == -1.0:
                 return str(self.a)+"-i"
            if float(self.b)-int(self.b) == 0:
                b = int(self.b)
            else:
                b = float(self.b)
            return str(self.a)+"-"+str(-1*b)+"i"

 def __add__(self, rhs):
     real = int(self.a)+int(rhs.a)
     img = int(self.b)+int(rhs.b)
     return Complex(real,img)
 def __mul__(self, rhs):
     a,b = int(self.a),int(self.b)
     c,d = int(rhs.a),int(rhs.b)
     real = a*c-b*d
     img = a*d+b*c
     return Complex(real,img)
 def __truediv__(self, rhs):
     a,b = int(self.a),int(self.b)
     c,d = int(rhs.a),int(rhs.b)
     real = (a*c+b*d)/(c**2+d**2)
     img = (b*c-a*d)/(c**2+d**2)
     return Complex(real,img)
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)


