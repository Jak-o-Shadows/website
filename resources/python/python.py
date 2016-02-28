#python.html

import os
import fnmatch
title = "Python -- Jak-o-Shadows"
style = """
<style type="text/css">
   li {
     line-height: 40px;
   }
</style>
"""

rootdir = "random/"
def findFiles(topDir, pattern):
    for dirpath, dirnames, filenames in os.walk(topDir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, pattern):
                yield os.path.join(dirpath, filename)[len(rootdir):]
blendList = list(findFiles(rootdir, "*.py"))
fnameList = []
for i in blendList:
    fnameList.append(i[:len(i) - len(".py")]) #replace with rstrip?

srcList = [[rootdir,x,".html"] for x in fnameList]
hrefList = ["<li><a href='"+"".join(x)+"'>"+x[1]+"</a></li>" for x in srcList]

contents = """
<h1>Python </h1>
    <p>&nbsp;</p>
    <ul>
      <li><a href="lapTimer/lapTimer.html">Lap timer with GUI.</a></li>
      <li><a href="../electronics/bike/bike_timer.html">Bike Timer (with GUI and backend).</a></li>
      <li><a href="wxpy/dblistctrl.html">How to use a Sqlite3 database to fill/populate a wxPython List Control (ListCtrl)</a></li>
      <li><a href="random/pythonTipsAndTricks.html">Some somewhat interesting and useful python tips and tricks</a></li>
      <li><a href="websiteSystem/main.html">A descirption of how the templating system of this website works</a></li>
      <li><a href="jgui.html">A very simple Graphic User Interface (GUI) kit for pygame. Implemented as sprites</a></li>
      <li><a href="randomNameGen/rndmNameGen.html">A simple name assigner/mixer, useful for Kris Kringle / Secret Santa draws</a></li>
      <l1><a href="random/jlog/jlogger.html">Create graphs of the movement of joystick axis'</a></li>
      <li><a href="robot/armik.html">Robotic Arm Inverse Kinematics</a></li>
      <li><a href="cgi-chat/cgi-chat.html">A CGI based instant messaging chatroom</a></li>
      <li><a href="tomodachi/life.html">Create graphs of Tomodachi Life relationships</a></li>"""+"".join(hrefList)+"""
    </ul>
"""
filesNeeded = []