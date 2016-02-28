#mkdir.py

import os

def mkdir(path):
    """"Requires a full path. *nix only (forward slash required)
    Requires a '/' at the start and at the end
    """
    l = []
    pathBits = path.split("/")
    for i in range(len(pathBits)):
        s = ""
        for j in range(i):
            s += pathBits[j] + "/"
        l.append(s)
    l.pop(0)
    l.pop(0)  
    for i in l:
        try:
            os.mkdir(i)
            print "folder", i, "has been created"
        except OSError:
            if i == "~/mounts/sfdeveloperweb/electronics/bike":
                print "GRR"
        
def makeDir(path):
    try:
        os.makedirs(path)
    except WindowsError:
        pass
        #print "folder might already there, ", path
    
    
    

