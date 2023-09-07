import os

def myFunc(e):
    return e[1]

lst = []
for r, d, f in os.walk("H:\\classi virtuali"):
    for file in f:
        lst.append([r, file])
lst.sort(key=myFunc)
html = ""
for f in lst:
    html += f"<a href='{f[0]}\\{f[1]}'>{f[1]}</a><br>"
html += "Number of Files: " + str(len(lst))

with open("output.html", "w", encoding="utf-8") as file:
    file.write(html)
os.startfile("output.html")
