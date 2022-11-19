que = []
time = []
finishtime=[]
averagetime = []
call = 0
orde = 0
count = 0

n = int(input())
for i in range(n):
    c = input()
    c = c.split()
    if c[0] == "reset":
        start = int(c[1])
    
    elif c[0] == "new":
        que.append(start+count)
        
        print("ticket",que[count])
        count = count+1
        time.append(int(c[1]))
        

    elif c[0] =="next":
        print("call",que[call])
        orde = call
        call = call+1

    elif c[0] =="order":
        
        finishtime.append(int(c[1]))
        dt = int(c[1])-time[orde]
        averagetime.append(dt)
        print("qtime",que[orde],dt)
        


    elif c[0] == "avg_qtime":
        average = 0
        for i in range(len(averagetime)):
            average = average+averagetime[i]
        result = (average)/len(averagetime)
        result = round(result,4)
        print("avg_qtime",result)

    else:
        pass

