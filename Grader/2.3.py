date = input()
date = date.split("/")
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
m =int(date[1])-1
print(month[m],date[0]+",",date[2])