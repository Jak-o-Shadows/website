title = "Blender Game Engine Thinking Part 2 -- Jak-o-Shadows"
contents = """
<p>Blender Game Engine Properties, 2.48 --> 2.49.x</p>
<p></p>---This follows on from my <a href="http://jak-o-shadows.users.sourceforge.net/blender/GE/thinking.html">previous writing</a>.</p>
<br />BLender 2.48, Blender 2.49.*
<br />
As some may have realised, any script that is linked to an always sensor (pulsed of course, so it runs more than once) is completely run. 
This means that any variables you define will get written back to to their default values. I can here you say <i>"But that doesn't matter, we'll just define em every time, we're assigning GE values to them anyway."</i>.
However, if you want to <i>+=</i> something, you need to define the variable first. However, if you only <i>+=</i> something once per execution, you'll be defining it to some value, and then adding something. You won't ever get anywhere.
Now, there is several ways to solve this problem. The simplest, and probably most useful for debugging, is storing the variable in a property. Properties remain between executions, as well as being able to be toggled visible during the playback of the GE.
<div class="syntax"><pre><span class="kn">import</span> <span class="nn">GameLogic</span>

<span class="n">cont</span> <span class="o">=</span> <span class="n">GameLogic</span><span class="o">.</span><span class="n">getCurrentController</span><span class="p">()</span>

<span class="n">own</span> <span class="o">=</span> <span class="n">cont</span><span class="o">.</span><span class="n">owner</span>



<span class="c">#guts of it here</span>

<span class="k">if</span> <span class="n">own</span><span class="p">[</span><span class="s">&quot;initp&quot;</span><span class="p">]</span> <span class="o">!=</span> <span class="bp">True</span><span class="p">:</span>

	<span class="c">#do setup here</span>

	<span class="n">own</span><span class="p">[</span><span class="s">&quot;prop&quot;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>


<span class="n">own</span><span class="p">[</span><span class="s">&quot;initp&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
</pre></div>
This code here allows is only ever run once. In the GE, this is useful if you're setting up a backend, doing other stuff that only needs to happen once, or just setting up a lot of variables. You could do it better than this (a simple always sensor) but this method is effective as well.
</p>
<p>If you want your program to be based upon user values, such as entering a name or server address, one of the simplest ways is to use a property. It's probably not the best way to for a production game, but if you feel confidant in your users, or just for testing, it works well.</p>
<p>Properties also have limited use as a method of communicating values between different scripts. Really, the only reaons you would want to do it this way is if you're absolutely pedantic about the namespace, or want to temporarily debug your script.<br /> You can access another objects property by first accessing the other object. Goes as follows (not actual code, dont' copy+paste): </p>
<em><p>import GameLogic
<br />
scene = GameLogic.getCurrentScene()
<br />
objlist = scene.objects
<br />

<br />
control = objlist["OBEmpty"]<br />
speed = control["wheelspeed"]<br />
</p></em>
<p>A much superior way is to store things into the GameLogic (?class?;?module?;?dict?), as simply as:</p>
<em><p>import Gamelogic<br />
GameLogic.varname = value</p></em>
<p>Another possible use for properties is that logic bricks can access them easily. One example is the Ipo actuator. In the drop down menu, there is an option for setting the frame to a property. This is ideal for turning an object a discrete number of degrees, or moving an object a discrete amount in a smooth line. You can also do tests based on property values (sensor).</p>
<p>A final word on the limitation of properties:<br />
<blockquote>It is best to only asign strings, boolean values, ints or floats to properties.
<br />
There are artificial limitations on the maximum and minimum values that you can graphically set a property to. For ints and floats it's 10000</blockquote></p>
<br />
<br />
<p>I write this in the hope that it will be useful. If it is wrong, feel free to contact me at simfake [.] mapping {@} gmail (.) com</p>
"""
style = """
<link rel="stylesheet" href="../../css/pygments_style.css">
"""
filesNeeded = []