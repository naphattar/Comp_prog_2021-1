def no_lowercase(t): # return True if no lowercase, otherwise return False
    i = 0
    error = []
    while i < len(t):
        if t[i] in "abcdefghijklmnopqrstuvwxyz":
            error.append(t[i])
            i = i+1
        else:
            i = i+1
    if len(error)>0:
        return False
    else:
        return True
def no_uppercase(t):
    i = 0
    error = []
    while i < len(t):
        if t[i] in "abcdefghijklmnopqrstuvwxyz".upper():
            error.append(t[i])
            i = i+1
        else:
            i = i+1
    if len(error)>0:
        return False
    else:
        return True
def no_number(t):
    i = 0
    error = []
    while i < len(t):
        if t[i] in "0123456789":
            error.append(t[i])
            i = i+1
        else:
            i = i+1
    if len(error)>0:
        return False
    else:
        return True
def no_symbol(t):
    i = 0
    error = []
    while i < len(t):
        if t[i] in "\'\"\\()[];:.,><=-_!@#$%^&*":
            error.append(t[i])
            i = i+1
        else:
            i = i+1
    if len(error)>0:
        return False
    else:
        return True
def sor(t):
    word = []
    out = ""
    for  i in range(len(t)):
        word.append(t[i])
    word.sort()
    for i in word:
        out += i
    return out   
def character_repetition(t):
    error = []
    if len(t)<4:
        return False
    else:
        for i in range(len(t)-3):
            inter = t[i:i+4]
            inter = sor(inter)
            if inter[0] == inter[3]:
                error.append(i)
                
            else:
                pass
        if len(error)>0:
            return True
        else:
            return False
def number_sequence(t):
    error = []
    
    number = "0123456789"
    if len(t)<4:
        return False
    else:
        for i in range(len(t)-3):
            inter = t[i:i+4]
            error2=[]
            for i in range(4):
                if inter[i] not in "0123456789":
                    error2.append(i)
            if len(error2) >0:
                pass
            else:
                i1 = number.find(inter[0])
                i2 = number.find(inter[1])
                i3 = number.find(inter[2])
                i4 = number.find(inter[3])
                
                if (i1+3)%10 == (i2+2)%10 == (i3+1)%10 == (i4)%10 :
                    error.append(i)
                elif (i4+3)%10 == (i3+2)%10 == (i2+1)%10 == (i1)%10:
                    error.append(i)
                else:
                    pass                          
        if len(error)>0:
            return True
        else:
            return False
def letter_sequence(t):
    error = []
    number = "abcdefghijklmnopqrstuvwxyz"
    if len(t)<4:
        return False
    else:
        for i in range(len(t)-3):
            inter = t[i:i+4]
            inter = inter.lower()
            error2=[]
            for i in range(4):
                if inter[i] not in number:
                    error2.append(i)
            if len(error2) >0:
                pass
            else:
                i1 = number.find(inter[0])
                i2 = number.find(inter[1])
                i3 = number.find(inter[2])
                i4 = number.find(inter[3])
                
                if (i1+3)%26 == (i2+2)%26 == (i3+1)%26 == (i4)%26 :
                    error.append(i)
                elif (i4+3)%26 == (i3+2)%26 == (i2+1)%26 == (i1)%26:
                    error.append(i)
                else:
                    pass                          
        if len(error)>0:
            return True
        else:
            return False
def keyboard_pattern(t):
    t = t.upper()
    error = []
    number1 = "!@#$%^&*()_+"
    number2 ="QWERTYUIOP"
    number3 = "ASDFGHJKL"
    number4 = "ZXCVBNM"
    if len(t)<4:
        return False
    else:
        for i in range(len(t)-3):
            inter = t[i:i+4]
            error2=[]
            for i in range(4):
                if inter[i] not in number1:
                    error2.append(i)
            if len(error2) >0:
                pass
            else:
                i1 = number1.find(inter[0])
                i2 = number1.find(inter[1])
                i3 = number1.find(inter[2])
                i4 = number1.find(inter[3])
                
                if (i1+3)%12 == (i2+2)%12== (i3+1)%12 == (i4)%12 :
                    error.append(i)
                elif (i4+3)%12 == (i3+2)%12 == (i2+1)%12 == (i1)%12:
                    error.append(i)
                else:
                    pass 
            error2 = [] 
            for j in range(4):
                if inter[j] not in number2:
                    error2.append(i)
            if len(error2) >0:
                pass
            else:
                i1 = number2.find(inter[0])
                i2 = number2.find(inter[1])
                i3 = number2.find(inter[2])
                i4 = number2.find(inter[3])
                
                if (i1+3)%10 == (i2+2)%10== (i3+1)%10 == (i4)%10 :
                    error.append(i)
                elif (i4+3)%10 == (i3+2)%10 == (i2+1)%10 == (i1)%10:
                    error.append(i)
                else:
                    pass 
            error2 = [] 
            for k in range(4):
                if inter[k] not in number3:
                    error2.append(i)
            if len(error2) >0:
                pass
            else:
                i1 = number3.find(inter[0])
                i2 = number3.find(inter[1])
                i3 = number3.find(inter[2])
                i4 = number3.find(inter[3])
                
                if (i1+3)%9 == (i2+2)%9== (i3+1)%9 == (i4)%9 :
                    error.append(i)
                elif (i4+3)%9 == (i3+2)%9 == (i2+1)%9 == (i1)%9:
                    error.append(i)
                else:
                    pass 
            error2 = []  
            for l in range(4):
                if inter[l] not in number4:
                    error2.append(i)
            if len(error2) >0:
                pass
            else:
                i1 = number4.find(inter[0])
                i2 = number4.find(inter[1])
                i3 = number4.find(inter[2])
                i4 = number4.find(inter[3])
                
                if (i1+3)%7 == (i2+2)%7== (i3+1)%7== (i4)%7 :
                    error.append(i)
                elif (i4+3)%7 == (i3+2)%7 == (i2+1)%7 == (i1)%7:
                    error.append(i)
                else:
                    pass   

        if len(error)>0:
            return True
        else:
            return False
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw):
    errors.append("Character repetition")
if number_sequence(passw):
    errors.append("Number sequence")
if letter_sequence(passw):
    errors.append("Letter sequence")
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
if len(errors) == 0:
    print("OK")
else:
    for i in errors:
        print(i)
