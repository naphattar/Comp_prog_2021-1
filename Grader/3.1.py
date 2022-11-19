number = input()
good = []
for j in ["01","02","51","53","55","58"]:
    good.append(j)
for i in range(20,41):
    good.append(str(i))

if number in good:
    print("OK")
else:
    print("Error")

