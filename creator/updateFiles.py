#script that takes a list of files , couple of other things and copies and junk
#try to follow

import shutil
import os

import mkdir

def read(fil):
    f = open(fil, "r")
    l = []
    for line in f:
        l.append(line.rstrip("\n"))
    f.close()
    return l
    
def copy(source, destination):
    """Copys a file from source to destination
    Uses shutil.copy
    """
    #makeFolder(os.sep.join(destination.split(os.sep)[:-1]))
    try:
        shutil.copy(source, destination)
        return True
    except IOError:
        return False
    #print source, "is copied"
    
def makeFolder(path):
    """Makes a folder using mkdir.mkdir(path)"""
    mkdir.mkdir(path)
    
def process(lis, path):
    """lis is a list of files to be copied. They have the full filepath.
    path is the filepath to the folder the file is in"""
    halfDest = read("destination.txt")[0]
    location = os.getcwd()
    lenLoc = len(os.getcwd())
    for i in path:
        makeFolder(halfDest + i[lenLoc:])
    for i in lis:
        destination = halfDest + i[lenLoc:]
        copy(i, destination)

