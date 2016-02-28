title = """Automatic build system used in making this website -- Jak-o-Shadows"""
style = ""

contents = """
Been under major revisions, still in process

<p>You may have noticed that my website is fairly similar graphically. If you look at the source, you might notice that great sections of it are identical. I'm going to explain, and share the methods
and programs i use to do this.</p>
<p>The main system i use to do this is <a href="http://www.cheetahtemplate.org/"> the cheetah template engine</a> (I'll explain alternatives at the end). After that i have a bunch of python files that basically define the content of each page.</p>
<p>
<b><u>The Files</u></b>
<br />
Each file contains 3 variables, the data of which is later inserted into the template.
<br />
Each contains a triple quoted string (which is used so double quotes can appear in the content). The three variables are 'contents', 'style' and 'title'. 'title', predictably enough, contains the title of the page. 'style' contains any extra css information that is required for the page, although it is not automatically inserted into "style" tags. 'contents' is where the main body of the website, which is this next here, contains.
<br />
Additionally, the location and filename of the python file is identical to the end location of the generated .html file. This could easily be changed, but it is a lot easier to manage content this way.</p>
<p>Perhaps later i'll change it so that the content, style and title of the page isn't stored within python files. After all, if you had a delimeter such as ';' it would be easy enough to do. Python files are easy however!</p>

"""
filesNeeded = []