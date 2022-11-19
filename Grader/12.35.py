class roman :
    def __init__(self, r):
        self.r = r

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return str(self.r)

    def __int__(self):
        rome = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        badrome = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        num = str(self.r)
        value = 0
        for m in badrome:
            if m in num:
                value = value + badrome[m]
                num = num.replace(m,"")
        for i in range(len(num)):
            value = value+ rome[num[i]]
        return value

    def __add__(self, rhs):
        c = int(a)+int(b)
        num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        al = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        newrome = ""
        for i in range(len(num)):
            c1,c = c//num[i],c%num[i]
            newrome = newrome + c1*al[i]
        return roman(newrome)
            
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))