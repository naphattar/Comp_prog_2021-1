file1,file2 = input().split()
def read_next(f):
 while True:
   t = f.readline()
   if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
     break
   x = t.strip().split() # ลบ blank ซ้ายขวา
   if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
     return x[0], x[1]
 return "", "" # แฟ้มหมดแล้ว คืนสตริงว่าง
student = []
f1 = open(file1, "r")
sid,score = read_next(f1)
while sid !="" and score !="":
    fal = sid[-2:]
    student.append([fal,sid,score])
    sid,score = read_next(f1)
f1.close()
f2 = open(file2, "r")
sid,score = read_next(f2)
while sid !="" and score !="":
    fal = sid[-2:]
    student.append([fal,sid,score])
    sid,score = read_next(f2)
f2.close()
student.sort()
for [fal,sid,score] in student:
    print(sid,score)