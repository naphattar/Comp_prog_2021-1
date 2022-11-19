score = input().split()
new = [float(x) for x in score]
new.sort()
average=(float(new[1])+float(new[2]))/2
#print("{:.2f}".format(average))
average = round(average,2)
print(average)