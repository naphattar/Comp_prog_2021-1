def make_int_list(x):
    x = x.split()
    newx = []
    for i in x:
        newx.append(int(i))
    return newx

 # รับสตริง x มำแยกและแปลงเป็น int เก็บใน list แล้วคืนเป็นผลลัพธ์
 # เช่น x = '12 34 5' ได้ผลเป็น [12 34 5]
def is_odd(e):
    e = int(e)
    if e%2 == 0:
        return False
    else:
        return True
 # คืนค่ำจริงเมื่อ e เป็นจ ำนวนคี่ ถ้ำไม่ใช่ คืนค่ำเท็จ
def odd_list(alist):
    newlist = []
    for i in alist:
        if is_odd(i):
            newlist.append(i)
    return newlist
 # คืน list ที่มีค่ำเหมือน alist แต่มีเฉพำะตัวที่เป็นจ ำนวนคี่
 # เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
def sum_square(alist):
    sum = 0
    for i in alist:
        sum = sum+i**2
    return sum
 # คืนผลรวมของก ำลังสองของแต่ละค่ำใน alist
 # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
exec(input().strip())