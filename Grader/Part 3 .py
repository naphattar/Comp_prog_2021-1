facultylink = []
linklist = []
subtoken = 1
subnumber = []
indexlist = []
x = 0
number =''
name = []
numberlist = []

for i in facultylist:
  if ("Faculty" in i) and ("Chulalongkorn" not in i):
    j = i.lower().replace(" ","-")
    name.append(j)
    link = "https://comprogchula.github.io/"+j+"-chulalongkorn-university.html"
    linklist.append(link)
j = 0
i = linklist[0]
html = str(urq.urlopen(i).read().decode('utf-8'))
x = html.find("class=\"text-black\"><strong>Tel:</strong></span> ")
while html[x+subtoken+47] != "<":
  number = number +html[x+subtoken+47]
  subtoken +=1
number = number.replace('+66','0')
print(name[0])
print(number[0:2]+number[6:])
j = j+1
number =''
subtoken =1 
while j < len(linklist):
  if j != 4:
    k

    i = linklist[j]
    html = str(urq.urlopen(i).read().decode('utf-8'))
    x = html.find("\"wpcf-field-wysiwyg wpcf-field-custom-content-contact-2\"><p><strong>Tel:</strong> ")
    while html[x+subtoken+81] != "<":


      number = number +html[x+subtoken+81]
      subtoken +=1
    number = number.replace('+66','0')
    print(name[j])
    print(number)
    j = j+1
    number = ''
    subtoken =1
  else:
    i = linklist[j]
    html = str(urq.urlopen(i).read().decode('utf-8'))
    x = html.find("Tel:</strong> ")
    while html[x+subtoken+13] != "<":


      number = number +html[x+subtoken+13]
      subtoken +=1
    number = number.replace('+66','0')
    print(name[j])
    print(number)
    j = j+1
    number = ''
    subtoken =1

