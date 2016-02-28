#jgui.html

title = "JGUI2: A simple pygame gui system -- Jak-o-Shadows"

style = ""
contents = """
<p> For a long time, i've been looking for a very simple and easy to
use GUI system for pygame.  I believe that pygame is rarely
the engine you use when you have to make an enormously complex game.
However it excels at simpler programs.</p>
<p>
Most GUI systems for pygame require you to use their event loop. But
for me, the gui is the last thing I do. So I needed something that
would just be another sprite. <br>
With that in mind, I went about designing my own. It needed to be very
simple, easy to integrate and easy to make. So I ended up with two
sprite classes that would accept images, and a bunch of functions that
generate images.</p>
<p>
The first sprite class is the static class. It's ideal for labels and
other static content that has no interactivity.<br>
The second sprite class is the button class. It's identical to the
static class except that it responds to mouse clicks.</p>
JGUI has a wide variety of functions that return surfaces for the 2
sprite classes to display. <br>
"""

filesNeeded = []