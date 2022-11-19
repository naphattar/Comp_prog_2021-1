class A: 
    def __init__(self, a, b):
        self.s = [a,b]
    def __str__(self):
        return ':'.join([(' '+str(e))[-2:] for e in self.s])
    def f(self):
        return A((int(self.s[0]))*-1,(int(self.s[1]))*-1)

a1 = A(9,1)
a2 = a1.f()
a3 = a2.f()
print(a1)
print(a2)
print(a3)   
        
        
