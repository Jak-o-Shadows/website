# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:30:09 2013

@author: Jak
"""
title = "Conky -- Jak_o_Shadows Web"

conkyrc = """
<div class="hlcode">
<div class="syntax"><pre><span class="err">#</span> <span class="nv">conky</span> <span class="nv">configuration</span>
<span class="err">#</span> <span class="nv">edited</span> <span class="nv">by</span> <span class="nv">kaivalagi</span>
<span class="err">#</span><span class="nv">edited</span> <span class="nv">some</span> <span class="nv">by</span> <span class="nv">Jak_o_Shadows</span>

<span class="err">#</span> <span class="nv">set</span> <span class="k">to</span> <span class="nv">yes</span> <span class="k">if</span> <span class="nv">you</span> <span class="nv">want</span> <span class="nv">Conky</span> <span class="k">to</span> <span class="nv">be</span> <span class="nv">forked</span> <span class="k">in</span> <span class="nv">the</span> <span class="nv">background</span>
<span class="nv">background</span> <span class="nv">no</span>

<span class="err">#</span> <span class="nv">Use</span> <span class="nv">Xft</span><span class="o">?</span>
<span class="nv">use_xft</span> <span class="nv">yes</span>

<span class="err">#</span> <span class="nv">Xft</span> <span class="nv">font</span> <span class="k">when</span> <span class="nv">Xft</span> <span class="nv">is</span> <span class="nv">enabled</span>
<span class="nv">xftfont</span> <span class="nv">Bitstream</span> <span class="nv">Vera</span> <span class="nv">Sans</span> <span class="nv">Mono</span><span class="p">:</span><span class="nv">size</span><span class="o">=</span><span class="mi">9</span>

<span class="err">#</span> <span class="nv">Text</span> <span class="nv">alpha</span> <span class="k">when</span> <span class="k">using</span> <span class="nv">Xft</span>
<span class="nv">xftalpha</span> <span class="mi">0</span><span class="p">.</span><span class="mi">8</span>

<span class="err">#</span> <span class="k">Update</span> <span class="nv">interval</span> <span class="k">in</span> <span class="nv">seconds</span>
<span class="nv">update_interval</span> <span class="mi">5</span><span class="p">.</span><span class="mi">0</span>

<span class="err">#</span> <span class="nv">This</span> <span class="nv">is</span> <span class="nv">the</span> <span class="nv">number</span> <span class="k">of</span> <span class="k">times</span> <span class="nv">Conky</span> <span class="nv">will</span> <span class="k">update</span> <span class="nv">before</span> <span class="nv">quitting</span><span class="p">.</span>
<span class="err">#</span> <span class="nv">Set</span> <span class="k">to</span> <span class="nv">zero</span> <span class="k">to</span> <span class="nv">run</span> <span class="nv">forever</span><span class="p">.</span>
<span class="nv">total_run_times</span> <span class="mi">0</span>

<span class="err">#</span> <span class="nv">Use</span> <span class="nv">double</span> <span class="nv">buffering</span> <span class="p">(</span><span class="nv">reduces</span> <span class="nv">flicker</span><span class="p">,</span> <span class="nv">may</span> <span class="o">not</span> <span class="nv">work</span> <span class="k">for</span> <span class="nv">everyone</span><span class="p">)</span>
<span class="nv">double_buffer</span> <span class="nv">yes</span>

<span class="err">#</span> <span class="k">Minimum</span> <span class="nv">size</span> <span class="k">of</span> <span class="nv">text</span> <span class="nv">area</span>
<span class="nv">minimum_size</span> <span class="mi">350</span> <span class="mi">5</span>
<span class="err">#</span><span class="nv">maximum_width</span> <span class="mi">350</span>

<span class="err">#</span> <span class="nv">Draw</span> <span class="nv">shades</span><span class="o">?</span>
<span class="nv">draw_shades</span> <span class="nv">yes</span>

<span class="err">#</span> <span class="nv">Draw</span> <span class="nv">outlines</span><span class="o">?</span>
<span class="nv">draw_outline</span> <span class="nv">no</span>

<span class="err">#</span> <span class="nv">Draw</span> <span class="nv">borders</span> <span class="nv">around</span> <span class="nv">text</span>
<span class="nv">draw_borders</span> <span class="nv">no</span>
<span class="nv">draw_graph_borders</span> <span class="nv">yes</span>

<span class="err">#</span> <span class="nv">Stippled</span> <span class="nv">borders</span><span class="o">?</span>
<span class="nv">stippled_borders</span> <span class="mi">0</span>

<span class="err">#</span> <span class="nv">border</span> <span class="nv">margins</span>
<span class="err">#</span><span class="nv">border_margin</span> <span class="mi">0</span>

<span class="err">#</span> <span class="nv">border</span> <span class="nv">width</span>
<span class="nv">border_width</span> <span class="mi">0</span>

<span class="err">#</span> <span class="k">Default</span> <span class="nv">colors</span> <span class="o">and</span> <span class="nv">also</span> <span class="nv">border</span> <span class="nv">colors</span>
<span class="nv">default_color</span> <span class="nv">white</span>
<span class="nv">default_shade_color</span> <span class="nv">black</span>
<span class="nv">default_outline_color</span> <span class="nv">white</span>

<span class="err">#</span> <span class="nv">own</span> <span class="k">window</span> <span class="nv">options</span>
<span class="nv">own_window</span>		<span class="nv">yes</span>
<span class="nv">own_window_transparent</span>	<span class="nv">yes</span>
<span class="nv">own_window_type</span>		<span class="nv">desktop</span>
<span class="nv">own_window_hints</span>	<span class="nv">undecorated</span><span class="p">,</span><span class="nv">below</span><span class="p">,</span><span class="nv">sticky</span><span class="p">,</span><span class="nv">skip_taskbar</span><span class="p">,</span><span class="nv">skip_pager</span>

<span class="err">#</span> <span class="nv">Text</span> <span class="nv">alignment</span><span class="p">,</span> <span class="nv">other</span> <span class="nv">possible</span> <span class="k">values</span> <span class="nv">are</span> <span class="nv">commented</span>
<span class="err">#</span><span class="nv">alignment</span> <span class="nv">top_left</span>
<span class="err">#</span><span class="nv">alignment</span> <span class="nv">top_right</span>
<span class="err">#</span><span class="nv">alignment</span> <span class="nv">bottom_left</span>
<span class="nv">alignment</span> <span class="nv">top_left</span>

<span class="err">#</span> <span class="nv">Gap</span> <span class="nv">between</span> <span class="nv">borders</span> <span class="k">of</span> <span class="nv">screen</span> <span class="o">and</span> <span class="nv">text</span>
<span class="err">#</span> <span class="nv">same</span> <span class="nv">thing</span> <span class="nv">as</span> <span class="nv">passing</span> <span class="o">-</span><span class="nv">x</span> <span class="k">at</span> <span class="nv">command</span> <span class="nv">line</span>
<span class="nv">gap_x</span> <span class="mi">10</span>
<span class="nv">gap_y</span> <span class="mi">25</span>

<span class="err">#</span> <span class="k">Subtract</span> <span class="nv">file</span> <span class="nv">system</span> <span class="nv">buffers</span> <span class="k">from</span> <span class="nv">used</span> <span class="nv">memory</span><span class="o">?</span>
<span class="nv">no_buffers</span> <span class="nv">yes</span>

<span class="err">#</span> <span class="nv">set</span> <span class="k">to</span> <span class="nv">yes</span> <span class="k">if</span> <span class="nv">you</span> <span class="nv">want</span> <span class="nv">all</span> <span class="nv">text</span> <span class="k">to</span> <span class="nv">be</span> <span class="k">in</span> <span class="nv">uppercase</span>
<span class="nv">uppercase</span> <span class="nv">no</span>

<span class="err">#</span> <span class="nv">number</span> <span class="k">of</span> <span class="nv">cpu</span> <span class="nv">samples</span> <span class="k">to</span> <span class="nv">average</span>
<span class="err">#</span> <span class="nv">set</span> <span class="k">to</span> <span class="mi">1</span> <span class="k">to</span> <span class="nv">disable</span> <span class="nv">averaging</span>
<span class="nv">cpu_avg_samples</span> <span class="mi">2</span>

<span class="err">#</span> <span class="nv">number</span> <span class="k">of</span> <span class="nv">net</span> <span class="nv">samples</span> <span class="k">to</span> <span class="nv">average</span>
<span class="err">#</span> <span class="nv">set</span> <span class="k">to</span> <span class="mi">1</span> <span class="k">to</span> <span class="nv">disable</span> <span class="nv">averaging</span>
<span class="nv">net_avg_samples</span> <span class="mi">2</span>

<span class="err">#</span> <span class="nv">Force</span> <span class="nv">UTF8</span><span class="o">?</span> <span class="nv">note</span> <span class="nv">that</span> <span class="nv">UTF8</span> <span class="nv">support</span> <span class="nv">required</span> <span class="nv">XFT</span>
<span class="nv">override_utf8_locale</span> <span class="nv">no</span>

<span class="err">#</span> <span class="k">Add</span> <span class="nv">spaces</span> <span class="k">to</span> <span class="nv">keep</span> <span class="nv">things</span> <span class="k">from</span> <span class="nv">moving</span> <span class="nv">about</span><span class="o">?</span>  <span class="nv">This</span> <span class="nv">only</span> <span class="nv">affects</span> <span class="nv">certain</span> <span class="nv">objects</span><span class="p">.</span>
<span class="nv">use_spacer</span> <span class="k">right</span>

<span class="nv">text_buffer_size</span> <span class="mi">2048</span>

<span class="err">#</span> <span class="nv">colours</span>
<span class="nv">color1</span> <span class="nv">white</span>
<span class="err">#</span> <span class="nv">light</span> <span class="nv">blue</span>
<span class="nv">color2</span> <span class="mi">6892</span><span class="nv">C6</span>
<span class="err">#</span> <span class="nv">orange</span>
<span class="nv">color3</span> <span class="nv">E77320</span>
<span class="err">#</span> <span class="nv">green</span>
<span class="nv">color4</span> <span class="mi">78</span><span class="nv">BF39</span>
<span class="err">#</span> <span class="nv">red</span>
<span class="nv">color5</span> <span class="nv">CC0000</span>

<span class="err">#</span> <span class="nv">variable</span> <span class="nv">is</span> <span class="nv">given</span> <span class="nv">either</span> <span class="k">in</span> <span class="k">format</span> <span class="err">$</span><span class="nv">variable</span> <span class="nv">or</span> <span class="k">in</span> <span class="err">${</span><span class="nv">variable</span><span class="err">}</span><span class="p">.</span> <span class="nv">Latter</span>
<span class="err">#</span> <span class="nv">allows</span> <span class="nv">characters</span> <span class="k">right</span> <span class="nv">after</span> <span class="nv">the</span> <span class="nv">variable</span> <span class="o">and</span> <span class="nv">must</span> <span class="nv">be</span> <span class="nv">used</span> <span class="k">in</span> <span class="nv">network</span>
<span class="err">#</span> <span class="nv">stuff</span> <span class="nv">because</span> <span class="k">of</span> <span class="nv">an</span> <span class="nv">argument</span>

<span class="err">#</span> <span class="nv">stuff</span> <span class="nv">after</span> <span class="s1">&#39;TEXT&#39;</span> <span class="nv">will</span> <span class="nv">be</span> <span class="nv">formatted</span> <span class="k">on</span> <span class="nv">screen</span>

<span class="nv">TEXT</span>

<span class="err">${</span><span class="nv">color1</span><span class="err">}${</span><span class="nv">font</span> <span class="nv">Bitstream</span> <span class="nv">Vera</span> <span class="nv">Sans</span> <span class="nv">Mono</span><span class="p">:</span><span class="nv">size</span><span class="o">=</span><span class="mi">21</span><span class="err">}</span>
<span class="err">${</span><span class="nv">execpi</span> <span class="mi">600</span> <span class="nv">gcalcli</span> <span class="o">--</span><span class="mi">24</span><span class="nv">hr</span> <span class="nv">calw</span> <span class="mi">2</span> <span class="err">|</span> <span class="nv">python</span> <span class="err">~</span><span class="p">/</span><span class="nv">conky</span><span class="p">/</span><span class="nv">translate</span><span class="p">.</span><span class="nv">py</span><span class="err">}</span>
<span class="err">${</span><span class="nv">font</span><span class="err">}</span>
</pre></div>
"""
gcalclirc = """
<div class="hlcode">
<div class="syntax"><pre><span class="p">[</span><span class="nv">gcalcli</span><span class="p">]</span>
<span class="nv">user</span><span class="p">:</span> <span class="nv">user</span><span class="p">.</span><span class="nv">name</span><span class="err">@</span><span class="nv">gmail</span><span class="p">.</span><span class="nv">com</span>
<span class="nv">pw</span><span class="p">:</span> <span class="nv">password</span>
<span class="nv">cals</span><span class="p">:</span> <span class="nv">owner</span>
</pre></div>
"""
translate = """
<div class="hlcode">
<div class="syntax"><pre><span class="c">#!/usr/bin/env python</span>
<span class="c"># -*- coding: utf-8 -*-</span>

<span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">re</span>


<span class="k">def</span> <span class="nf">main</span><span class="p">():</span>

	<span class="n">detector</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\033</span><span class="s">\[\d+(?:;\d+)?m&#39;</span><span class="p">)</span>
	<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">xreadlines</span><span class="p">():</span>
		<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">detector</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">,</span><span class="n">line</span><span class="p">))</span>

<span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
	<span class="n">main</span><span class="p">()</span>
</pre></div>

</div>
"""


contents = """
I finally decided that I wanted my calendar to show on my desktop. So, I used conky, and a program called gcalcli to do it.
<br />
<p>
First, install conky:
    <br />
    "sudo apt-get install conky"
    <br />or<br />
    "su -c 'yum install conky'"
    <br />
Next, install gcalcli:
    <br />
    "sudo apt-get install gcalcli"
    <br />or<br />
    "su -c 'yum install gcalcli'"
    <br />
</p>
<p>
<h1>Various Configuration Files</h1>
<br />
Create a file named .conkyrc in your home directory. I use the following config:
    <p>
    %s
    </p>
Create a file named .gclalclirc in your home directory. Fill in the details:
    <p>
    %s
    </p>
<h1>For Cinnamon/ATI users</h1>
<br />
Unfortunatley, the <em>--nc</em> option for gcalcli appears not to be working. This results in messed up formatting in conky.
The solution is to strip this out using a small python script, with a regex. I put this script in ~/conky/translate.py
<p>
%s
</p>
Autostart conky however you want! I use Cinnamon's auto-start, but likely cron or similar would work.
</p>

""" % (conkyrc, gcalclirc, translate)
style = """<link rel="stylesheet" href="../css/pygments_style.css">"""
filesNeeded = []
