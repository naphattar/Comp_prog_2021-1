import numpy as np
def read_data():
 # อ่านข ้อมูลจากแป้นพิมพ์ จากนั้นสร้างและคืนอาเรย์สองตัว
 # weight เป็นอาเรยส์ ามชอ่ งเก็บน ้าหนักของคะแนนกลางภาค ปลายภาค และโครงงาน (float)
 # data เป็นอาเรย์ขนาด n4 เก็บข ้อมูลนักเรียน n คน แต่ละคนมีข ้อมูล
 # เลขประจ าตัว คะแนนกลางภาค ปลายภาค และโครงงาน (int)
    w = [float(e) for e in input().split()]
    w = [1]+w
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    data = data*weight
    ID = data[::,0]
    m1 = data[::,1]
    m2 = data[::,2]
    m3 = data[::,3]
    score = m1+m2+m3
    meann = np.mean(score)
    result = ID[score<meann]
    if result.shape[0] > 0:
        finalresult = ""
        for i in result:
            finalresult = finalresult+str(int(i))+", "
        print(finalresult[:-2])
    else:
        print("None")




    

 # แสดงเลขประจ าตัวที่ได ้คะแนนรวมต ่ากว่าคะแนนเฉลี่ย
 # ให ้แสดงบนบรรทัดเดียวกันหมดคั่ นด ้วยเครื่องหมายจุลภาคและชอ่ งวา่ งหนงึ่ ชอ่ ง
 # เรียงตามล าดับที่ปรากฎใน data ถ้าไม่มีใครได ้ต ่ากว่าคะแนนเฉลี่ยเลย ให ้แสดงค าว่า None

exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
