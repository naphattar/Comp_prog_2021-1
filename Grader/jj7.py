alp = "abcdefghijklmnopqrstuvwxyz"
def get_secret(t):
    result = ""
    sec = t[0]
    t = t[1:]
    t = t.split(sec)
    for i in range(len(t)):
        if i%2 == 1:
            result += t[i]
    return result


    
def print_secret(filename):
    data = open(filename,"r")
    for line in data:
        print(get_secret(line))
    data.close()
 # filename เก็บสตริงที่เป็นชื่อแฟ้มข้อมูล
 # ฟังก์ชันนี้อ่านสตริงจากแฟ้มมาทีละบรรทัด และ print ข้อความลับที่ได้จากการถอดรหัสสตริงในแต่ละบรรทัด
exec(input().strip()) # DON'T remove this line