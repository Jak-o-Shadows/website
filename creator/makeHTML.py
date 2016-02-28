import sys
import template

toRemove = "~/websites/sourceforge/"

def write(info, filename):
    f= open(filename, "w")
    f.write(info)
    f.close()

updated = []

i = sys.argv[1]
i = i.split()[0]
k =i.split("/")
i = k.pop()
i = i.split(".")[0]
path = toRemove
for h in k:
    path += h
    path += "/"
sys.path.append(path)
j = __import__(i)
output = template.main({"title" : j.title, "contents" : j.contents, "style": j.style})
write(str(output),path+ i+".html")
updated.append(i+".html")
    
for i in updated:
    #print i + " has been updated."
    pass


