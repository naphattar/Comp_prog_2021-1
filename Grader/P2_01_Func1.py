def is_odd(n):
    if n%2 != 0:
        return True
    else:
        return False
 # คืน (True/False) ว่า n เป็นจ านวนคี่หรือไม่

def has_odds(x):
    odd = []
    for i in range(len(x)):
        if x[i]%2 != 0:
            odd.append(i)
    if len(odd) > 0:
        return True
    else:
        return False


 # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลบางตัวเป็นจ านวนคี่

def all_odds(x):
    odd = []
    for i in range(len(x)):
        if x[i]%2 != 0:
            odd.append(i)
    if len(odd) == len(x):
        return True
    else:
        return False
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลทุกตัวเป็นจ านวนคี่

def no_odds(x):
    odd = []
    for i in range(len(x)):
        if x[i]%2 != 0:
            odd.append(x[i])
    if len(odd) > 0:
        return False
    else:
        return True
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข ้อมูลที่เป็นจ านวนคี่เลย

def get_odds(x):
    odd = []
    for i in range(len(x)):
        if x[i]%2 != 0:
            odd.append(x[i])
    return odd
 # คืนลิสต์ที่มีจ านวนคี่ที่มีเก็บในลิสต์ x (ล าดับก่อนหลังให ้เป็นไปตามล าดับเดียวกับใน x)
 # เชน่ x = [1,2,3,5,0] จะได ้ผลคือ [1,3,5]

def zip_odds(a, b):
    odd = []
    odda = get_odds(a)
    oddb = get_odds(b)
    if len(odda)>= len(oddb):
        for i in range(len(oddb)):
            odd.append(odda[i])
            odd.append(oddb[i])
        for i in range(len(oddb),len(odda)):
            odd.append(odda[i])
    elif len(odda)< len(oddb):
        for i in range(len(odda)):
            odd.append(odda[i])
            odd.append(oddb[i])
        for i in range(len(odda),len(oddb)):
            odd.append(oddb[i])


    
    return odd
 # คืนลิสต์ที่สร้างจากการน าจ านวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
 # เชน่ a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได ้คือ
 # [1,19,5,11,7,17,9,3]

exec(input().strip())