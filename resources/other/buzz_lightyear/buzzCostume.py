title = "Buzz Lightyear Costume -- Jak_o_Shadows"
style = """"""
folderLoc = "other\\buzz_lightyear\\"


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

contents = """Graphics obtained from <a href="http://www.therpf.com/f24/buzz-lightyear-costume-ideas-89095/index3.html">http://www.therpf.com/f24/buzz-lightyear-costume-ideas-89095/index3.html</a>
			""" + "<br />".join([imageContent % (x, x) for x in filesNeeded]) + """
			<p>
			Mostly constructed out of felt.
			Armguards are stiff white card.
			Working laser
			
			
			</p>"""