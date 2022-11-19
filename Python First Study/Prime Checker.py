import math
a = input("ใส่เลขที่คุณต้องการจะตรวจสอบว่าเป็นจำนวนเฉพาะหรือไม่ : ")
a = int(a)
b = (math.floor(math.sqrt(a)))
if a == 1:
    print(str(a)+"ไม่เป็นทั้งจำนวนเฉพาะเเละจำนวนประกอบ")
else:
     for i in range(2,a):
        if a%i == 0 :
             print(str(a)+"เป็นจำนวนประกอบ")
             break 
        else:
            if i == a-1 :
                print(str(a)+"เป็นจำนวนเฉพาะ")
            

    
    
