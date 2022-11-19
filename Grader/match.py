def get_secret(t):
    keyword = t[0]
    sentence = t[1:]
    result = ""
    sentence = sentence.split(keyword)
    newword = [sentence[i] for i in range(len(sentence)) if i%2==1]
    for i in newword:
        result += i
    return result


    
def print_secret(filename):
    file = open(filename,"r")
    for line in file:
        print(get_secret(line))
    file.close()
 # filename เก็บสตริงที่เป็นชื่อแฟ้มข้อมูล
 # ฟังก์ชันนี้อ่านสตริงจากแฟ้มมาทีละบรรทัด และ print ข้อความลับที่ได้จากการถอดรหัสสตริงในแต่ละบรรทัด
exec(input().strip()) # DON'T remove this line