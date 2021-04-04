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
    l[0] + l[-1]+".html" #was x[1] + x[-1] + ".html"
    page = ".html"
    for i in l:
        #print(s + i[0]+i[1]+page + m + i[1].lstrip(sep).rstrip(sep).capitalize() + e + gap
        t += s + i[0]+i[1]+page + m + i[1].lstrip(sep).rstrip(sep).capitalize() + e + gap + "\n"
    return t


def createNeighboursList(i, fileList, sep=os.sep):
    firsts = [[x[1].rstrip(i[1]), x[-1]] for x in fList2 if sep.join(x[1].split(sep)[:-1]) == sep.join(i[1].split(sep)[:-1])]    
    print("a", firsts)
    firsts = [["",x[-1]] for x in fList2 if sep.join(x[1].split(sep)[:-1]) == sep.join(i[1].split(sep)[:-1])]
    print("d", firsts )
    t = ""
    for j in range(len(i[1].split(sep)) -2 -1):
        t += ".." + sep
    #extra = sep.join(i[1].split(sep)[:-1])
    #print(extra, "ex"
    #lens = len(extra)
    #sep = "/"
    seconds = [[t+sep.join(x[1].split(sep)[2:]), x[-1]]  for x in fList2 if sep.join(x[1].split(sep)[:-2]) == sep.join(i[1].split(sep)[:-2])]
    seconds = seconds + [[t + sep.join(x[1].split(sep)[2:]), x[-1]] for x in fList2 if sep.join(x[1].split(sep)[:-2]) == sep.join(i[1].split(sep)[:-3])]
    sep = os.sep
    #print(i[-1]
    #for j in seconds: print(j[0], j[1]
    #print
    #print
    
    firsts = htmlList(firsts)
    seconds = htmlList(seconds)
    
    return firsts, seconds




def createPaths(filePath, rootdir, sep=os.sep):
    paths = {}
    k = filePath.split(sep)
    #gets the last item (ie the filename) and removes the extension (.py). ie filename
    kfname =  k.pop()
    fname = kfname[:-3]
    #removes the resources section of the path of the files
    toRemove = len(rootdir)
    #filePath is the path of the resource
    filePath = filePath[:-(len(fname)+3)]
    #p is the output path of the file
    folder =  filePath[toRemove:]
    filepath = back+sep+ "res" + folder
    outputpath = back + sep +"website" + "%s" + folder
    #appends folder of .py, output folder, rsources folder, filename
    paths[0] = filePath
    paths[1] = outputpath
    paths[2] = filepath
    paths[3] = fname
    
    #does it nicer
    paths["pydir"] = paths[0]
    paths["output"] = paths[1]
    print(paths[1])
    paths["filesNeeded"] = paths[2]
    paths["fname"] = paths[3]

    return paths    
    
    
    
def makePage(paths, date):
    sys.path.append(paths["pydir"])
    fil = __import__(paths["fname"])
    
    firsts = ""
    seconds = ""
    
    try:
        try:
            for lang in fil.contents.iterkeys():
                output = template.main({"title":fil.title[lang], "contents":fil.contents[lang], \
                                        "style":fil.style, "time":date, "first":firsts, "second":seconds})
                #print(fil.title
                filesNeeded = fil.filesNeeded
                for f in filesNeeded:
                    src = paths["filesNeeded"] + f
                    out = paths["output"] + f
                    if not updateFiles.copy(src, out):
                        print("%s was not copied" % src)
                mkdir.makeDir(paths["output"] %(os.sep + lang+os.sep))
                write(str(output), paths["output"] %(os.sep + lang+os.sep)+paths["fname"]+".html")
        except AttributeError:
            #this page is not multi-lingual yet - hence is english
            output = template.main({"title":fil.title, "contents":fil.contents, \
                                    "style":fil.style, "time":date, "first":firsts, "second":seconds})
            #print(fil.title
            filesNeeded = fil.filesNeeded
            for f in filesNeeded:
                src = paths["filesNeeded"] + f
                out = paths["output"] + f
                if not updateFiles.copy(src, out):
                    print("%s was not copied" % src)
            mkdir.makeDir(paths["output"] % (os.sep + "en" + os.sep))
            write(str(output), paths["output"] %(os.sep +"en" + os.sep) +paths["fname"]+".html")
            
        return True
    except Exception as e:
        print(sys.exc_info()[0])
        print(e)
        #print([fil.title, fil.contents, fil.style, date, firsts, seconds]
        print("GAH", paths["pydir"], paths["fname"], "s", "GAH")
        return False
        

def updateOneFile(filePath):
    sep = os.sep
    back = ".."
    rootdir = back + sep + "resources"

    paths = createPaths(filePath, rootdir)
    
    date = ":".join(str(datetime.datetime.utcnow()).split(":")[:-1])

    status = makePage(paths, date)
    return status

if __name__ == "__main__":
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
        fList2.append(createPaths(i, rootdir))
        
        
    date = ":".join(str(datetime.datetime.utcnow()).split(":")[:-1])
    
    for i in fList2:
        status = makePage(i, date)
    print('DONE')
