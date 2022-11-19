data = input()
k,sum=0,0
all =[]
while data!="q":
    number = float(data)
    k = k+1
    all.append(number)
    data = input()
if k>0:
     for i in range(0,k):
         sum = sum+ all[i]
     print(round((sum/k),2))
if k==0:
    print("No Data")