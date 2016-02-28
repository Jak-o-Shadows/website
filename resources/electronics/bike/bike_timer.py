title = "Bike Timer -- Jak-o-Shadows"
style = """<style type="text/css">
   li {
     line-height: 40px;
   }
</style>"""
contents = """
<h1> Bike Timer</h1>
    <p><a href="diagram.svg"><img src="diagram.png" alt="diagram of sensor" width="257" height="149" /></a></p>
    <p>Above is a simple circuit diagram. There is also a <a href="bikeTimer.sch">gEDA schematic version</a>, and the <a href="bikeTimer.png">subsequent rendering.</a></p>
    <p>This circuit (and accompanying program) will tell you every time the tire of your bike completes one revolution. This doesn't sound very useful does it? However, this enables you to calculate the rpm, cadence, distance travelled and average speed. While you can buy little things that clip onto your bike that do this, this has the advantage of being connected to a computer. This is an advantage because you can more easily log your training (realistically, this is mostly used for a training bike on a stand). It also allows you to make a game out of it (I intend to, when i get the input working properly). Anyway, onto how it works.</p>
<p>This circuit emulates an old gameport joystick. All it needs is some wires, a computer with a gameport, a 30-80k resistor and a photoresistor (Commonly found in solar panels, and streetlamps). The pins 3 and 1 would normally be connected via a pot, which would be changed depending on the movement of the joystick on the x axis.</p>
<p>&nbsp;</p>
<p>From now on, i'm going to assume you're working on a GNU/Linux computer (what else are you going to run on your 8 year old computer?). However, the end program <strong>should</strong> work perfectly on any variety of windows that supports recent versions of python and pygame (2.6x, 1.8).</p>
<p>&nbsp;</p>
<p>If you're using linux, you probably won't have the driver for analog joysticks enabled. To do this, open a terminal and type (note that you must enter your root password. Ubuntu users can use sudo instead)</p>
<blockquote>
  <p><em>su -c 'modprobe analog'</em></p>
</blockquote>
<p>This loads the module for analog joysticks. To check if this has worked, in the terminal type <em>dmesg.</em> If there is any kind of weird error message, double and triple check your circuit. If it worked, there should be a message identifying the type of joystick your distro has detected. Mine detects a 2 axis, 2 button joystick.</p>
<p>&nbsp;</p>
<p>Alright. We've got the physical part connected and your OS is picking it up. Now we need to test whether it's working (Note that it's preferable to use tested parts in this. A digital multimeter is very useful, but not essential). To do this, open a terminal and type <em>jstest /dev/input/js0</em>. (If you  get an error message such as no device found, the input may be somewhere else. Thats where it was on my Fedora 12 box). To actually use the device, you need a torch. A LED torch is great, as is a laser, but a cheap laser pointer will typically not last very long due to overheating. To obtain greater reliability, put the photoresistor in a bit of plastic garden pipe or hose. Anyway, when you block the light between the LED and the photoresistor, one of the values in <em>jstest</em> should change. If you're done like i have, it should be the first number.</p>
<p>&nbsp;</p>
<p>Ok. We've got the computer picking up the input. Now we have to do some clever programming. When i saw we, i mean I.<strong> </strong>I'll outline my methods and post what code i have though.</p>
<p align="center"><a href="intelligence.py">Code</a> (Need to open with a python editor if not using *nix)</p>

<p>Using pygame, we can make a class that harvests the information. However there is one big (<strong>huge</strong>) problem that prevents us from just calling the get_status() function. <em>It calls it too fast!</em> For every revolution, there is about a 5cm gap where the light can shine through. The rest of the tire is blacked out with paper that prevents the light from shining through. When just starting off, there is tens of thousands of<strong>True</strong> signals being recieved by pygame. However, when going flat out (or at least as fast as i can go on my bike without it coming off the stand.), the timer recieves it in perfect time. To me, that signals that some clever programming is needed. With several chats to the people in the #electronics channel on the freenode irc, i determined that something that checks the time between subsequent signals is the way to go. If the time between them is vastly off what is expected, discard it. It is implemented successfully, however i no longer have the bike inside. It's kinda hard to test these things by waving your hands in front of the LDR, you don't move anywhere fast enough.</p>
<p>&nbsp;</p>
<blockquote>
  <p><strong>Download</strong></p>
  <p>The GUI requires that the file <em>intelligence.py</em> be in the same folder as gui.py. I don't actually have cadence working, because that requires working out the gear ratio. You'rs will probably be different as well. Also speed isn't worked out in the normal km/h.</p>
<ul>
  <li><a href="gui.py">GUI </a></li>
  <li><a href="intelligence.py">BACKEND</a></li>
</ul>
  <p><strong>Improvements</strong></p>
</blockquote>
<p>It's perfectly feasible to use a reed switch instead. Heck, it's even possible to just substitute the reed switch with the photoresistor (not tested). However, if you look at a diagram of a gameport, you'll see it's got seperate pins for buttons. If using a reed switch (or any other type of digital switch), i would recommend plugging into pins 2 and 4. This would require fairly minor changes to the code, mostly in <em>intelligence.py</em> function <em>get_status()</em>.</p>
"""
filesNeeded = ["bikeTimer.sch", "bikeTimer.png", "intelligence.py", "gui.py"]