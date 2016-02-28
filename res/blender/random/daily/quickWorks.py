#Quick Works
import os
import fnmatch

#import copyMedia


#rootdir += "/blender/random/daily/"
rootdir = "../res/blender/random/daily/"
def findFiles(topDir, pattern):
    for dirpath, dirnames, filenames in os.walk(topDir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, pattern):
                yield os.path.join(dirpath, filename)[len(rootdir):]
blendList = list(findFiles(rootdir, "*.blend"))
fnameList = []
print blendList
for i in blendList:
    fnameList.append(i[:len(i) - len(".blend")])
    
items = {}
filesNeeded = []
for i in fnameList:
    filesNeeded.append(i +".blend")
    filesNeeded.append(i+".jpg")
    extension = ".jpg"
    try:
        items[i] = [i + ".blend", i + extension, i + ".txt"]
    except IOError:
        extension = ".png"
        items[i] = [i + ".blend", i + extension, i + ".txt"]
    filesNeeded.append(i+extension)

    
text = """<table style="text-align: left; width: 700px;" border="1"
cellpadding="2" cellspacing="2">
<tbody>
<tr>
<td style="vertical-align: top; width: 33%;">The Blend<br>
</td>
<td style="vertical-align: top;">The Render<br>
</td>
<td style="vertical-align: top;">Notes<br>
</td>
</tr>
"""

def read(file):
    try:
        f = open(rootdir + file, "r")
        text = ""
        for line in f:
            text +=  " " + line.rstrip("\n")
        f.close()
        return text
    except:
        return "No Notes for this file"


for i in items:
    text += """
    <tr>
<td style="vertical-align: top;"><a href = "%s">%s</a><br>
</td>
<td style="vertical-align: top; width: 233px"><a href = "%s"><img src ="%s" width=200, height = 200 /></a><br>
</td>
<td style="vertical-align: top;">%s<br>
</td>
</tr>
""" % (items[i][0], items[i][0], items[i][1], items[i][1], read(items[i][2]))



text += """
</tbody>
</table>
"""
title = """Very quick modelling works in blender -- Jak-o-Shadows"""
style = """
"""
contents = text
print text


