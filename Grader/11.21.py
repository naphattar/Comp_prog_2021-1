import numpy as np
def sum_2_rows( M ):
    m1 = M[::2,::]
    m2 = M[1::2,::]
    return m1+m2
 # คืนผลที่ได ้จากการรวมจ านวนในคอลัมน์เดียวกันของแถวที่ติดกันทีละคู่แถว
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 4, 6, 8, 10],
 # [ 4, 5, 6, 7], [20, 22, 24, 26]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
def sum_left_right( M ):
    m1 = M[::,0:(M.shape[1])//2]
    m2 = M[::,(M.shape[1])//2:]
    return m1+m2
 # คนืผลทไี่ ดจ้ากการรวมจ านวนของครงึ่ ซา้ยกับครงึ่ ขวาของ M
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 2, 4],
 # [ 4, 5, 6, 7], [10, 12],
 # [ 8, 9, 10, 11], [18, 20],
 # [12, 13, 14, 15]] [26, 28]]
def sum_upper_lower( M ):
    m1 = M[0:(M.shape[0])//2,::]
    m2 = M[(M.shape[0])//2:,::]
    return m1+m2
 # คืนผลที่ได ้จากการรวมจ านวนของครึ่งบนกับครึ่งล่างของ M
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[ 8, 10, 12, 14],
 # [ 4, 5, 6, 7], [16, 18, 20, 22]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
def sum_4_quadrants( M ):
    m1 = M[0:(M.shape[0])//2,0:(M.shape[0])//2]
    m2 = M[(M.shape[0])//2:,0:(M.shape[0])//2]
    m3 = M[0:(M.shape[0])//2,(M.shape[0])//2:]
    m4 = M[(M.shape[0])//2:,(M.shape[0])//2:]
    return m1+m2+m3+m4

 # คืนผลที่ได ้จากการแบ่ง M เป็น 4 จตุภาค และรวมจ านวนที่ต าแหน่งตรงกันในแต่ละจตุภาค
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[20, 24],
 # [ 4, 5, 6, 7], [36, 40]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
def sum_4_cells( M ):
    m1 = M[0::2,0::2]
    m2 = M[1::2,0::2]
    m3 = M[0::2,1::2]
    m4 = M[1::2,1::2]
    return m1+m2+m3+m4

    
 # คืนผลที่ได ้จากการรวมจ านวนที่ติดกัน 4 ตัว ตามรูปแบบในตัวอย่างข ้างล่างนี้
 # เชน่ M = [[ 0, 1, 2, 3], ได ้ [[10, 18],
 # [ 4, 5, 6, 7], [42, 50]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
def leap(years):
    years = years - 543
    if years%4 == 0:
        if years%100 ==0:
            if years%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def count_leap_years( years ):
    y = years-543
    return sum(((y%4==0)&(y%400==0))|((y%4==0)&(y%100!=0)))
 # years เป็นอาเรย์เก็บปี พ.ศ.
 # คืนจ านวนปีใน years ที่เป็นปีอทิกสุรทิน (ปีที่ ก.พ. มี 29 วัน)
exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ