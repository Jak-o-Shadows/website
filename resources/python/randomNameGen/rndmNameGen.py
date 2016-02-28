title = "Random Name Mixer -- Jak-o-Shadows"
style = """
"""
contents = """
I quickly made this random draw generator one day because I got tired
of drawing names out of a hat.<br>
<table style="text-align: left; width: 100%;" border="0" cellpadding="2"
cellspacing="2">
<tbody>
<tr>
<td style="vertical-align: top; width: 33%;"><a href="#About:">About</a><br>
</td>
<td style="vertical-align: top; width: 33%;"><a href="#Notes:">Notes</a><br>
</td>
<td style="vertical-align: top; width: 33%;"><a href="#Download:">Download</a><br>
</td>
</tr>
</tbody>
</table>
<br>
<br>
<span style="font-weight: bold; text-decoration: underline;"><a
name="About:"></a>About:</span><br>
This program allows for random assignment of 1 value to another. This
would most often be used to assign one person to give a gift to another.<br>
<br>
The two functions that acutally mix the names up are in the file
backEnd.py.&nbsp; You simply feed a list of names into the function
randomize. textBased.py allows names to be entered and then mixed once.
When entering names, an empty name will tell the program to proceed to
mixing the names. gui.py offers the functionality of textBased.py, but
it also allows names to be remixed without re-entering them. This lets
you, <span style="font-style: italic;">fine tune</span>, the results
until you find something of your liking. <br>
<br>
Here is a screenshot of gui.py when it first starts:<br>
<img style="width: 336px; height: 526px;"
alt="A picture of gui.py when it first opens"
title="A picture of gui.py when it first opens" src="start.png"><br>
<br>
Names have been added, but not yet mixed:<br>
<img style="width: 337px; height: 525px;"
alt="Names added to gui.py, but not yet mixed."
title="Names added to gui.py, but not yet mixed."
src="namesEntered.png"><br>
<br>
Names have been mixed:<br>
<img style="width: 337px; height: 525px;"
alt="&quot;gui.py&quot;. Names have been mixed."
title="&quot;gui.py&quot;. Names have been mixed." src="randomized.png"><br>
I agree, the pattern is obvious, However it works well enough.<br>
<br>
<span style="font-weight: bold; text-decoration: underline;"><a
name="Notes:"></a>Notes:</span><br>
<ul>
<li>Automatically capitalizes input.</li>
<li>Does not allow duplicate names.</li>
</ul>
<span style="font-weight: bold; text-decoration: underline;"><a
name="Download:"></a>Download:</span><br>
<ul>
<li><a href="backEnd.py">backEnd.py</a>&nbsp;&nbsp;
----&nbsp;&nbsp;&nbsp; Necessary for all files</li>
<li><a href="textBased.py">textBased.py</a>&nbsp;
----&nbsp;&nbsp;&nbsp; Text based version.</li>
<li><a href="gui.py">gui.py&nbsp;</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp; &nbsp;&nbsp;&nbsp; ----&nbsp;&nbsp;&nbsp; Graphic User Interface
version. Requires wxPython<br>
</li>
</ul>
"""
filesNeeded = ["start.png", "namesEntered.png", "randomized.png", "backEnd.py", "textBased.py", "gui.py"]