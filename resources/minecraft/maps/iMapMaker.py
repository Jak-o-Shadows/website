tx=14320
ty=23424
xgap=512
ygap=512
xiter=tx/xgap
yiter=ty/ygap

coords = []
url = ""

#for i in range(yiter):
#    for j in range(xiter):
#        x1 = j*xgap
#        x2 = x1 + xgap
#        y1 = i*ygap
#        y2 = y1+ygap
#        coords.append([x1, x2, y1, y2, str(j)+str(i)])
#        
#texts = []

#for i in coords:
#    text = "<area shape='rect' coords='" + str(i[0])
#    text += "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])
#    text += "' href ='" + url + i[4] + "' />"
#    texts.append(text)

#content = """This is a simple image map, explain more later<br />
#<img src="map.png" usemap="#only" />
#<map name="#only">"""

#for i in texts:
 #   content += i
#
#content += "</map>"
#print content

title = "minecraft map test thing"
style = ""
contents = ""
filesNeeded = []
