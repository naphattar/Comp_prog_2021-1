number = input()
if len(number)==10:
    cut = number[0:2]
    test = ["06","08","09"]
    if cut in test:
        print("Mobile number")
    else:
        print("Not a mobile number")
else:
    print("Not a mobile number")