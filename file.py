file1 = open(r"WhatsApp Chat with Friend.txt", "r") # Here, change the name of the WhatsApp export file.
file2 = open(r"Links.txt", "a") # This file will be generated with all the links in the export file.
file1.seek(0,0)
data = file1.read()
a = []

while not data.find('http')== -1:
    data = data.replace(data[0:(data.find('http')-1)], "")[1:]
    a.append(data[0:data.find('\n')])
    data = data.replace(data[0:(data.find('\n'))], "")

for i in range(len(a)):
    a[i] = a[i] + "\n"

for j in range(len(a)):
    file2.write(a[j]) 

file1.close()
file2.close()
