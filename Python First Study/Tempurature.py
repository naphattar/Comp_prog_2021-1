temp = input("ใส่เลขอุณหภูมิพร้อมหน่วย:")
degree = temp[:-1]
unit = temp[-1].upper()
degree =int(degree)
if unit == "C":
    degree = ((degree*9)/5)+32
    print(str(degree)+"F")
if unit == "F":
    degree = (degree -32)*5/9
    print(str(degree)+"C")
