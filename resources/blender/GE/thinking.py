
contents = """
<h1> Thinking Blender Game Engine    </h1>
    <p>I've been working for a while on making decent games with blender. At first it was just with logic bricks and a smattering of python, now i've progressed to a smattering of logic bricks and a heap of python. For me, a heap of python is a lot more logical and easier. It is also more capable of making more complicated games. To get proper AI and pathfinding and other things, it is a lot more practical to use python rather than hugely complicated logic brick webs.</p> <p>My major block with that stopped me from understanding how to program for the game engine, is that you don't write the main loop/function. Really, each script associated to a an always sensor (you should always have an always sensor running a python script (unless of course you're having performance problems. then it might be applicable to have a script only run when it is needed.)), is just a part of a main loop. Therefore you should not do anything that stalls the execution. For example
    </p>
    <div class="syntax">
      <pre><span class="kn">import</span> <span class="nn">GameLogic</span>

<span class="n">cont</span> <span class="o">=</span> <span class="n">GameLogic</span><span class="o">.</span><span class="n">getCurrentController</span><span class="p">()</span>
<span class="n">own</span> <span class="o">=</span> <span class="n">cont</span><span class="o">.</span><span class="n">owner</span>

<span class="n">fward</span> <span class="o">=</span> <span class="n">own</span><span class="o">.</span><span class="n">sensor</span><span class="p">[</span><span class="s">&quot;fwardarrow&quot;</span><span class="p">]</span>

<span class="n">pos</span> <span class="o">=</span> <span class="n">own</span><span class="o">.</span><span class="n">position</span>

<span class="n">posx</span><span class="p">,</span> <span class="n">posy</span><span class="p">,</span> <span class="n">posz</span> <span class="o">=</span> <span class="n">pos</span>

<span class="k">if</span> <span class="n">fward</span><span class="o">.</span><span class="n">positive</span><span class="p">:</span>

    <span class="n">posx</span> <span class="o">+=</span> <span class="mi">1</span>

<span class="n">pos</span> <span class="o">=</span> <span class="n">posx</span><span class="p">,</span> <span class="n">posy</span><span class="p">,</span> <span class="n">posz</span>

<span class="n">own</span><span class="o">.</span><span class="n">position</span> <span class="o">=</span> <span class="n">pos</span> 
</pre></div>
<p>This code will work perfectly... until you activate the fwardarrow sensor (known in the script as fward). We are assuming this sensor is a simple keyboard sensor, probably mapped to the forward arrow (duh). When you activate the sensor, it will stall the game engine because the execution loop is being stalled. However, near to the name of the sensor, there is 2 buttons with <i>,,,</i> . These buttons either pulse True, or pulse False. Pulsing True is what we want in this case. This will cause the sensor to flash on an off, very quickly. This eliminates the execution loop freezing.</p>
"""

title = "Blender Game Engine Thinking"

style = """<link rel="stylesheet" href="../../css/pygments_style.css">"""
filesNeeded = []