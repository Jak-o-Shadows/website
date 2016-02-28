#tips and tricks

title = """
Python Tips and Tricks
"""

contents = """
<h1>Pausing Pygame</h1>
<p>Sometimes when developing games, what you see on the screen happens too fast for you to make sense of it. You can try print statements, or you can take the time to learn an external debugger, which would probably be overkill for what you want it to do <em>right now</em>. One solution i've found when writing games for pygame is to just not let the main <em>while</em> loop finish until you're ready. To that end, I did this:
</p>
<p>
<div class="hlcode">
<div class="highlight"><pre>    <span class="n">keepGoing</span> <span class="o">=</span> <span class="bp">True</span>
    <span class="k">while</span> <span class="n">keepGoing</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">pygame</span><span class="o">.</span><span class="n">event</span><span class="o">.</span><span class="n">get</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">type</span> <span class="o">==</span> <span class="n">pygame</span><span class="o">.</span><span class="n">QUIT</span><span class="p">:</span>
                <span class="n">keepGoing</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="n">pygame</span><span class="o">.</span><span class="n">display</span><span class="o">.</span><span class="n">update</span><span class="p">()</span>
        <span class="n">NextFrame</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="k">while</span> <span class="ow">not</span> <span class="n">NextFrame</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">pygame</span><span class="o">.</span><span class="n">event</span><span class="o">.</span><span class="n">get</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">type</span> <span class="o">==</span> <span class="n">pygame</span><span class="o">.</span><span class="n">QUIT</span><span class="p">:</span>
                    <span class="n">keepGoing</span> <span class="o">=</span> <span class="bp">False</span>
                <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">type</span> <span class="o">==</span> <span class="n">pygame</span><span class="o">.</span><span class="n">KEYDOWN</span><span class="p">:</span>
                    <span class="n">NextFrame</span> <span class="o">=</span> <span class="bp">True</span>
</pre></div></div></div></div>
</p>
<p>
This code allows no further input when it is running. Since you're waiting on this to finish, this means that you have literally no input. Also, it isn't possible to go backward. A keypress on any key will let it move onto the next frame. To use, just add the last while loop to the end of your main loop, as shown
</p>
<div><p><h1>Storing a timedelta in a sqlite3 database</h1></p>
<p>I found myself needing to store a datetime.timedelta object in a sqlite3 database. However, despite having adaptors for datetime.datetime objects, timedelta misses out. Through googling/irc, i found that it would be best to store the timedelta as a string. An alternative is to store the start and end times of the timedelta as datetime.datetime objects (which can be stored easily), however I chose not to.</p>
<p>The Code</p>
<div class="hlcode">
<div class="syntax"><pre><span class="k">def</span> <span class="nf">convertTime</span><span class="p">(</span><span class="n">t</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Converts a timedelta to a string. ignores days and annoying decimal places</span>
<span class="sd">    compatible with strToTD</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">st</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
    <span class="n">st</span> <span class="o">=</span> <span class="n">st</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;.&quot;</span><span class="p">)</span>
    <span class="n">st</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">st</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][:</span><span class="mi">2</span><span class="p">]</span>
    <span class="n">s</span> <span class="o">=</span> <span class="s">&quot;:&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">st</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">s</span>
    
<span class="k">def</span> <span class="nf">strToTD</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;converts a string that was a timedelta (having been converted using</span>
<span class="sd">    convertTime) back into a timedelta</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">s</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">s</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&quot;:&quot;</span><span class="p">)]</span>
    <span class="n">ms</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span>
    <span class="n">sec</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="n">ms</span><span class="o">/</span><span class="mf">100.0</span>
    <span class="n">m</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="n">h</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="n">td</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span> <span class="o">=</span> <span class="n">h</span><span class="p">,</span> <span class="n">minutes</span> <span class="o">=</span> <span class="n">m</span><span class="p">,</span> <span class="n">seconds</span> <span class="o">=</span> <span class="n">sec</span><span class="p">)</span><span class="c">#, microseconds = us)</span>
    <span class="k">return</span> <span class="n">td</span>
</pre></div>

</div>
<p>While this is only good for up house:minute:seconds:micro/milli-seconds, it is an alternative to storing the start and end times</p>

"""

style = """<link rel="stylesheet" href="../../css/pygments_style.css">"""
filesNeeded = []
