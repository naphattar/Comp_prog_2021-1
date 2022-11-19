def get_secret(t):
    output = ""
    special = t[0]
    using = t[1:].split(special)
    forresult = using[1::2]
    for i in range(len(forresult)):
        output += forresult[i]
    return output


    
def print_secret(filename):
    notebook = open(filename,"r")
    for line in notebook:
        print(get_secret(line))
    notebook.close()
 # filename เก็บสตริงที่เป็นชื่อแฟ้มข้อมูล
 # ฟังก์ชันนี้อ่านสตริงจากแฟ้มมาทีละบรรทัด และ print ข้อความลับที่ได้จากการถอดรหัสสตริงในแต่ละบรรทัด
exec(input().strip()) # DON'T remove this line