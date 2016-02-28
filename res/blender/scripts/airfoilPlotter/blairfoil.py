style = """
<style type="text/css">
   li {
     line-height: 40px;
   }
</style>
"""
title = """Blender Airfoil Plotter - Jak-o-Shadows"""
contents = """
<h2 align="center">Blender Airfoil Plotter</h2>
<p align="center"><a href="plotter.zip">Download Airfoil Plotter</a></p>
<p>A script by Fake (http://fake.yolasite.com). If you did not get it from there, please email me at simfake[dot]mapping[at]gmail[dot]com.
  <br />
  <br />
  It takes a series of coordinates, as almost from <a href="http://www.ae.illinois.edu/m-selig/ads.html">the UIUC site</a> download the .dat file for the airfoil you want.
  t<br />
  <br />
  To get it into blender, just remove the junk lines before the coordinates, and the blank line between the sets of coordinates.
  <br /> 
  <br />
  Since it now draws edges, just remove doubles and the big line down the center.
  <br />
  <br />
  To change the file, just change the variable named file to what you want. Make sure you type an aboslute path.
  <br />
  <br />
  This program is free software: you can redistribute it and/or modify
  <br />
  it under the terms of the GNU General Public License as published by<br /> the Free Software Foundation, either version 3 of the License, or
  <br />
  (at your option) any later version.
  <br />
  <br /> 
  This program is distributed in the hope that it will be useful,
  <br />
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  <br />
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  <br />
  GNU General Public License for more details.
  <br />
  <br />
  You should have received a copy of the GNU General Public License
  <br />
  along with this program. If not, see 
  <a href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>
</p>
<p><br />
               Released 2009 by Fake (http://fake.yolasite.com or http://jak-o-shadows.users.sourceforge.net)
               <br />
</p>
<p>An example of what the program does:<br /> <br /> From this (modified b29root.dat))<br />  0.0000000 0.0000000<br />  0.0082707 0.0233088<br />  0.0132000 0.0298517<br />  0.0255597 0.0425630<br />  0.0503554 0.0603942<br />  0.0751941 0.0739301<br />  0.1000570 0.0850687<br />  0.1498328 0.1023515<br />  0.1996558 0.1149395<br />  0.2495240 0.1230325<br />  0.2994312 0.1272298<br />  0.3993490 0.1253360<br />  0.4993711 0.1130538<br />  0.5994664 0.0934796<br />  0.6996058 0.0695104<br />  0.7997553 0.0445423<br />  0.8998927 0.0207728<br />  0.9499514 0.0098870<br />  1.0000000 0.0000000<br />  0.0000000 0.0000000<br />  0.0061140 -.0208973<br />  0.0062188 -.0210669<br />  0.0087532 -.0247377<br />  0.0138088 -.0307807<br />  0.0264052 -.0416431<br />  0.0515127 -.0548774<br />  0.0765762 -.0637165<br />  0.1016176 -.0703581<br />  0.1516652 -.0801452<br />  0.2016828 -.0869356<br />  0.2516733 -.0910290<br />  0.3016387 -.0926252<br />  0.4015163 -.0905235<br />  0.5013438 -.0834273<br />  0.6011363 -.0728351<br />  0.7008976 -.0591463<br />  0.8006328 -.0428603<br />  0.9003380 -.0235778<br />  0.9501740 -.0122883<br />  1.0000000 0.0000000<br /> <br /> <br /> To this(with doubles removed and the line down the middle removed):</p>
<p><img src="example.JPG" width="582" height="174" alt="example" /> </p>
For help and a sort of FAQ, go to <a href="http://blenderartists.org/forum/showthread.php?t=171239">http://blenderartists.org/forum/showthread.php?t=171239</a>. 
"""
filesNeeded = ["plotter.zip", "example.JPG"]