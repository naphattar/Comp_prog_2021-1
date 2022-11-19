def is_prime(n):
 # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่
 if n <= 1:
    return False
 for k in range(2,int(n**0.5)+1):
    if n%k == 0:
       return False
    else:
       return True
def next_prime(N):
    k = int(N)+1
    while is_prime(k) == False:
        k = k+1
    return k 



 # คืนจานวนเฉพาะตัวที่มีค่าน้อยสุดที่มากกว่า N

def next_twin_prime(N):
    m = int(next_prime(N))
    while is_prime(m+2) == False:
        m = int(next_prime(m))

    return(m,m+2)
 # คืนจ านวนเฉพาะสองค่าที่เป็น twin prime ที่มีค่าน้อยสุดที่มากกว่า N
 # twin prime คือจ านวนเฉพาะที่มีค่าต่างกัน 2 เชน่ 11 กับ 13 หรือ 41 กับ 43
exec(input().strip())