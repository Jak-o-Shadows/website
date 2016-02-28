#rebuild all
# -*- coding: utf-8 -*-
import template
import updateFiles
import mkdir

import os
import sys
import fnmatch
import datetime

def read():
    f = open("exceptions.txt")
    a = []
    for line in f:
        a.append(line.rstrip("\n"))
    return a

def write(info, filename):
    f = open(filename, "w")
    f.write(info)
    f.close()
    
    
def htmlList(l):
    """Takes a list of html addresses, and turns it into bunch of hyperlinks"""
    t = ""
    gap = "<br />"
    s = '<a href="'
    m = '">'
    e = "</a>"
    x[0] + x[-1]+".html" #was x[1] + x[-1] + ".html"
    page = ".html"
    for i in l:
        #print s + i[0]+i[1]+page + m + i[1].lstrip(sep).rstrip(sep).capitalize() + e + gap
        t += s + i[0]+i[1]+page + m + i[1].lstrip(sep).rstrip(sep).capitalize() + e + gap + "\n"
    return t


#rootdir = os.getcwd()
#rootdir = ".." + rootdir  #bad for windows

#rootdir = "/home/hayden/websites/sourceforge/resources"

sep = os.sep
back = ".."

#gets a list of all the files to be made into webpages
rootdir = back + sep + "resources"
def findFiles(topDir, pattern):
    for dirpath, dirnames, filenames in os.walk(topDir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, pattern):
                yield os.path.join(dirpath, filename)
fileList = list(findFiles(rootdir, "*.py"))

fList2 = []
for i in fileList:
    k = i.split(sep)
    #gets the last item (ie the filename) and removes the extension (.py). ie filename
    kfname =  k.pop()
    fname = kfname[:-3]
    #removes the resources section of the path of the files
    toRemove = len(rootdir)
    #i is the path of the resource
    i = i[:-(len(fname)+3)]
    #p is the output path of the file
    folder = i[toRemove:]
    filepath = back+sep+ "res" + folder
    outputpath = back + sep +"website" + folder
    #appends folder of .py, output folder, rsources folder, filename
    fList2.append([i, outputpath, filepath, fname])
    
    
date = ":".join(str(datetime.datetime.utcnow()).split(":")[:-1])

for i in fList2:
    """i = [html res path, outputPath, fileNeeded path, fileName]"""
    sys.path.append(i[0])
    fil = __import__(i[3])
    firsts = [[x[1].rstrip(i[1]), x[-1]] for x in fList2 if sep.join(x[1].split(sep)[:-1]) == sep.join(i[1].split(sep)[:-1])]
    firsts = [["",x[-1]] for x in fList2 if sep.join(x[1].split(sep)[:-1]) == sep.join(i[1].split(sep)[:-1])]
    t = ""
    for j in xrange(len(i[1].split(sep)) -2 -1):
        t += ".." + sep
    #extra = sep.join(i[1].split(sep)[:-1])
    #print extra, "ex"
    #lens = len(extra)
    sep = "/"
    seconds = [[t+sep.join(x[1].split(sep)[2:]), x[-1]]  for x in fList2 if sep.join(x[1].split(sep)[:-2]) == sep.join(i[1].split(sep)[:-2])]
    seconds = seconds + [[t + sep.join(x[1].split(sep)[2:]), x[-1]] for x in fList2 if sep.join(x[1].split(sep)[:-2]) == sep.join(i[1].split(sep)[:-3])]
    sep = os.sep
    #print i[-1]
    #for j in seconds: print j[0], j[1]
    #print
    #print
    
    firsts = htmlList(firsts)
    seconds = htmlList(seconds)
    firsts = ""
    seconds = ""

    try:
        output = template.main({"title":fil.title, "contents":fil.contents, \
    "style":fil.style, "time":date, "first":firsts, "second":seconds})
        #print fil.title
        filesNeeded = fil.filesNeeded
        for f in filesNeeded:
            src = i[2] + f
            out = i[1] + f
            if not updateFiles.copy(src, out):
                print "%s was not copied" % src
        mkdir.makeDir(i[1])
        write(str(output), i[1]+i[3]+".html")
    except Exception, e:
        print sys.exc_info()[0]
        print e
        #print [fil.title, fil.contents, fil.style, date, firsts, seconds]
        print "GAH", i[0], i[3], "s", "GAH"
    """
    filesNeeded = fil.filesNeeded
    for f in filesNeeded:
        src = i[2] + f
        out = i[1] + f
        updateFiles.copy(src, out)
    mkdir.makeDir(i[1])
    write(str(output), i[1]+i[3]+".html")
    """
    
    
print 'DONE'
    
    
    
    
    
"""Uneccssary as we're using local stuff now
toRemove = "/home/hayden/websites/sourceforge/resources/"
files = []
for i in fileList:
    files.append(i[len(toRemove):])
    
fileList = files
"""

"""
#changed from complicated because of findFiles()
actual = fileList

#likely unessary now.
for i in read():
    try:
        actual.remove(i)
    except:
        pass



fileList = []
for i in actual:
    i = i.split(".")
    if i[len(i)-1] == "py":
        fileList.append(i[len(i)-2])
        
        
fileEnd = []
for i in fileList:
    k = i.split("\\")
    fname = k.pop()
    pathEnd = "../htdocs"
    for j in k:
        pathEnd += j + "/"
        fileEnd.append(pathEnd)
        
    



def write(info, filename):
    f = open(filename, "w")
    f.write(info)
    f.close()
    
updated = []
paths = []
date = time.localtime()
date = str(date[0]) + ", " + str(date[1]) + ", " + str(date[2])
for i in range(len(fileList)):
    k =fileList[i].split("/")
    fname = k.pop()
    path = toRemove
    for h in k:
        path += h
        path += "/"
    sys.path.append(path)
    paths.append(path)
    j = __import__(fname)
    output = template.main({"title" : j.title, "contents" : j.contents, "style": j.style, "time" : date})
    filesNeeded = j.filesNeeded
    
    mkdir.mkdir(fileEnd[i])
    write(str(output), fileEnd[i] + fname +".html")
    updated.append(fileEnd[i]+ fname +".html")
    
    
for i in updated:
    #print i + " has been updated."
    pass
    

    
#updateFiles.process(updated, paths)

print "All files copied over to the remote computer"

"""