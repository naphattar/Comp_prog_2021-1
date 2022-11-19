def read_date():
     # อ่านวันเดือนปีคั่นด้วยช่องว่าง เดือนเป็นชื่อเดือน คืนลิสต์ เลขวัน เดือน ปี
     mname = ["Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
     date1 = input().split()
     d = int(date1[0])
     m = mname.index(date1[1][:3]) + 1
     y = int(date1[2])
     date = [d,m,y]
     return date


def zodiac(d,m):
     # คืนชื่อราศีของวัน d เดือน m
     Zodiac = ["Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn"]
     if d >=22 and m>= 3:
         return Zodiac[m-1]
     elif d>= 21 and m <= 2:
         return Zodiac [m-1]
     elif d <= 21 and m >= 3:
         return Zodiac[m-2]
     elif d<= 20 and m <= 2:
         return Zodiac[m-2]

             
def days_in_feb(y):
     # คืนจานวนวันของเดือนกุมภาพันธ์ในปี y
     if y % 400 == 0 or y % 100 != 0 and y%4 == 0 :
         return 29
     if y  % 400 == 0 or y % 100 != 0 and y%4 == 0 :
         return 29
     else:
         return 28



def days_in_month(m,y): 
    # คืนจ านวนวันของเดือน m ในปี y
    if m ==2:
        return days_in_feb(y)
    if m in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
def days_in_between(d1,m1,y1,d2,m2,y2):
    days = 0
    if m1 < 12 : 
        days += 31
    if m1 < 11 :
         days += 30
    if m1 < 10 : 
        days += 31
    if m1 < 9 :
         days += 30
    if m1 < 8 :
         days += 31
    if m1 < 7 : 
        days += 31
    if m1 < 6 : 
        days += 30
    if m1 < 5 : 
        days += 31
    if m1 < 4 : 
        days += 30
    if m1 < 3 : 
        days += 31
    if m1 < 2 : 
        days += days_in_feb(y1)
    if m2 > 1 : 
        days += 31
    if m2 > 2 : 
        days += days_in_feb(y2)
    if m2 > 3 : 
        days += 31 
    if m2 > 4 :
         days += 30
    if m2 > 5 :
         days += 31
    if m2 > 6 :
         days += 30
    if m2 > 7 :
         days += 31
    if m2 > 8 : 
        days += 31
    if m2 > 9 : 
        days += 30
    if m2 > 10 : 
        days += 31
    if m2 > 11 : 
        days += 30
    days += (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return days



 # คืนจ านวนวันตั้งแต่วันเดือนปีd1,m1,y1 ถึง d2,m2,y2
def main() :
 d1,m1,y1 = read_date()
 d2,m2,y2 = read_date()
 z1 = zodiac(d1,m1)
 z2 = zodiac(d2,m2)
 print(z1,z2)
 print(days_in_between(d1,m1,y1,d2,m2,y2))
 # แสดง ราศีของ d1,m1,y1 กับ ของ d2,m2,y2 บรรทัดเดียกัน คั่นด้วยช่องว่าง
 # แสดงจ านวนวันตั้งแต่ d1,m1,y1 ถึง d2,m2,y2
exec(input().strip()) 
