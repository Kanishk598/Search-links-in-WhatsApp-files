file1 = open(r"input.txt", "r") # Here, change the name of the WhatsApp export file.
file2 = open(r"Links.html", "a") # This file will be generated with all the links in the export file.
file1.seek(0,0)
data = file1.read()
a = []

file2.write("<!DOCTYPE html>")
file2.write("<html>")
file2.write("<body>")

while not data.find('http')== -1:
    data = data.replace(data[0:(data.find('http')-1)], "")[1:]
    a.append(data[0:data.find('\n')])
    data = data.replace(data[0:(data.find('\n'))], "")
    a[-1] = '<a href="' + a[-1] + '" target="_blank">' + a[-1] + '</a>'
    file2.write(a[-1])
    file2.write('<br>')

file2.write('</body>')
file2.write('</html>')
file1.close()
file2.close()
