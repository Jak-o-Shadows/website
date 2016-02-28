title = "My 3D Printer -- Jak-o-Shadows web"
style = ""

folderLoc = "electronics\\3dprinter\\"


import glob
import os

path = os.getcwd()
where = "\creator"
pos = path.find(where)
fileNeededLoc = path[:pos] + "\\res\\" +folderLoc
os.chdir(fileNeededLoc)
filesNeeded = glob.glob("*")
os.chdir(path)

imageContent = """<a href = "%s" > <img src ="%s" width="80%%" /> </a>"""

contents = """
	<p>My 3D printer is probably unique, so I decided to share it. Take particular note of the y-ends and the orientation of the x-axis - do not copy this</p>
	<p>Images:<br />
	""" + "<br />".join([imageContent % (x, x) for x in filesNeeded]) + """</p>"""