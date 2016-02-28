title = "How to populate/fill a wxPython ListCtrl using a database"
style = """<link rel="stylesheet" href="../../css/pygments_style.css">"""
filesNeeded = ["dblistctrl1.py", "dblistctrl1.png"]
contents = """Sometimes you want to use a database to fill a ListCtrl. If your data is able to be sorted, this has the lage advantage of handling the sorting for you.
<div><img src="dblistctrl1.png" /></div>
<div class="hlcode">
<div class="syntax"><pre><span class="c"># -*- coding: utf-8 -*-</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">Created on Tue Jul 10 13:55:00 2012</span>

<span class="sd">@author: Jak_o_Shadows</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="kn">import</span> <span class="nn">sqlite3</span>
<span class="kn">import</span> <span class="nn">random</span>
<span class="kn">import</span> <span class="nn">wx</span>


<span class="k">class</span> <span class="nc">MyFrame</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">Frame</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
        <span class="n">kwds</span><span class="p">[</span><span class="s">&quot;style&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">DEFAULT_FRAME_STYLE</span>
        <span class="n">wx</span><span class="o">.</span><span class="n">Frame</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">ListCtrl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">wx</span><span class="o">.</span><span class="n">LC_REPORT</span><span class="o">|</span><span class="n">wx</span><span class="o">.</span><span class="n">SUNKEN_BORDER</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span><span class="o">.</span><span class="n">InsertColumn</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="s">&quot;a&quot;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span><span class="o">.</span><span class="n">InsertColumn</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;b&quot;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span><span class="o">.</span><span class="n">InsertColumn</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="s">&quot;c&quot;</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">__set_properties</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">__do_layout</span><span class="p">()</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">Bind</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">EVT_LIST_COL_CLICK</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">setupSort</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span><span class="p">)</span>
        
        <span class="c">#for allowing sorting in descending order        </span>
        <span class="bp">self</span><span class="o">.</span><span class="n">oldC</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">reverse</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">command</span> <span class="o">=</span> <span class="s">&quot;SELECT * FROM tbl&quot;</span>
        
        <span class="c">#populate the database</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">setupDB</span><span class="p">()</span>
        
    <span class="k">def</span> <span class="nf">__set_properties</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">SetTitle</span><span class="p">(</span><span class="s">&quot;Fill a list control with a database!&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__do_layout</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">sizer_1</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">BoxSizer</span><span class="p">(</span><span class="n">wx</span><span class="o">.</span><span class="n">VERTICAL</span><span class="p">)</span>
        <span class="n">sizer_1</span><span class="o">.</span><span class="n">Add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">wx</span><span class="o">.</span><span class="n">EXPAND</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">SetSizer</span><span class="p">(</span><span class="n">sizer_1</span><span class="p">)</span>
        <span class="n">sizer_1</span><span class="o">.</span><span class="n">Fit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">Layout</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">setupSort</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;Sets the command for filling the list control, based on</span>
<span class="sd">        what column is clicked</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">c</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">GetColumn</span><span class="p">()</span>   <span class="c">#get the column that was clicked on</span>
        
        <span class="k">if</span> <span class="n">c</span><span class="o">==</span><span class="mi">0</span><span class="p">:</span>
            <span class="c">#order by first column</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">command</span> <span class="o">=</span> <span class="s">&quot;SELECT * FROM tbl ORDER BY a&quot;</span>
        <span class="k">elif</span> <span class="n">c</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
            <span class="c">#order by second column</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">command</span> <span class="o">=</span> <span class="s">&quot;SELECT * FROM tbl ORDER BY b&quot;</span>
        <span class="k">elif</span> <span class="n">c</span><span class="o">==</span><span class="mi">2</span><span class="p">:</span>
            <span class="c">#order by third column</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">command</span> <span class="o">=</span> <span class="s">&quot;SELECT * FROM tbl ORDER BY c&quot;</span>
                
        
        <span class="c">#Toggle reverse</span>
        <span class="k">if</span> <span class="n">c</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">oldC</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">reverse</span> <span class="o">=</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">reverse</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">reverse</span> <span class="o">=</span> <span class="bp">False</span>
            
        <span class="c">#if reverse, append &quot;DESC&quot; to the select command</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">reverse</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">command</span> <span class="o">+=</span> <span class="s">&quot; DESC&quot;</span>
            
        <span class="bp">self</span><span class="o">.</span><span class="n">oldC</span> <span class="o">=</span> <span class="n">c</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fillLC</span><span class="p">()</span>
        <span class="n">event</span><span class="o">.</span><span class="n">Skip</span><span class="p">()</span>
        
    <span class="k">def</span> <span class="nf">setupDB</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;Open the database, add a table&quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">con</span> <span class="o">=</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s">&quot;:memory:&quot;</span><span class="p">)</span>   <span class="c">#open a connection to a DB in RAM</span>
        <span class="n">command</span> <span class="o">=</span> <span class="s">&quot;CREATE TABLE tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, a INT, b TEXT,</span><span class="se">\</span>
<span class="s">                    c REAL)&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">command</span><span class="p">)</span>    <span class="c">#add a table (tbl) with 4 columns)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fillDB</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">fillDB</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">letters</span> <span class="o">=</span> <span class="s">&quot;abcdefghijklmnopqrstuvwxyz&quot;</span>
        <span class="n">command</span> <span class="o">=</span> <span class="s">&quot;INSERT INTO tbl VALUES(Null, ?, ?, ?)&quot;</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="mi">100</span><span class="p">):</span>
            <span class="n">a</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">26</span><span class="p">)</span>    <span class="c">#add a random int from 1 to 26</span>
            <span class="n">b</span> <span class="o">=</span> <span class="n">letters</span><span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">randrange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">26</span><span class="p">)]</span> <span class="c">#add a random letter from letters</span>
            <span class="n">c</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span><span class="o">*</span><span class="mi">26</span>      <span class="c">#add a random float from (0,26)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="n">command</span><span class="p">,</span> <span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">c</span><span class="p">))</span>    <span class="c">#add the data to the DB</span>

        <span class="c">#use executemany</span>
        <span class="n">data</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">xrange</span><span class="p">(</span><span class="nb">long</span><span class="p">(</span><span class="mf">1e2</span><span class="p">)):</span>
            <span class="n">a</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">26</span><span class="p">)</span>    <span class="c">#add a random int from 1 to 26</span>
            <span class="n">b</span> <span class="o">=</span> <span class="n">letters</span><span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">randrange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">26</span><span class="p">)]</span> <span class="c">#add a random letter from letters</span>
            <span class="n">c</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span><span class="o">*</span><span class="mi">26</span>      <span class="c">#add a random float from (0,26)</span>
            <span class="n">data</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">c</span><span class="p">))</span>  <span class="c">#add the data to a list</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">executemany</span><span class="p">(</span><span class="n">command</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span> <span class="c">#all data in the list is added to db</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>   <span class="c">#commits the data, saving it</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fillLC</span><span class="p">()</span>   <span class="c">#update the list control</span>
        
        
    <span class="k">def</span> <span class="nf">fillLC</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;Fills the list control based on the sorting command&quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span><span class="o">.</span><span class="n">DeleteAllItems</span><span class="p">()</span>  <span class="c">#since we&#39;re sorting, must delete all</span>
        <span class="c">#then get a list of tuples of all the data</span>
        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">con</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">command</span><span class="p">)</span><span class="o">.</span><span class="n">fetchall</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
            <span class="c">#loop through and add it</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">listCtrl</span><span class="o">.</span><span class="n">Append</span><span class="p">(</span><span class="n">i</span><span class="p">[</span><span class="mi">1</span><span class="p">:])</span>   
            
<span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span>
    <span class="c">#wxGlade default stuff</span>
    <span class="n">app</span> <span class="o">=</span> <span class="n">wx</span><span class="o">.</span><span class="n">PySimpleApp</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
    <span class="n">wx</span><span class="o">.</span><span class="n">InitAllImageHandlers</span><span class="p">()</span>
    <span class="n">frame_1</span> <span class="o">=</span> <span class="n">MyFrame</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="s">&quot;&quot;</span><span class="p">)</span>
    <span class="n">app</span><span class="o">.</span><span class="n">SetTopWindow</span><span class="p">(</span><span class="n">frame_1</span><span class="p">)</span>
    <span class="n">frame_1</span><span class="o">.</span><span class="n">Show</span><span class="p">()</span>
    <span class="n">app</span><span class="o">.</span><span class="n">MainLoop</span><span class="p">()</span>
</pre></div>
<div>
Now lets go through how it works. Starting from the top, we import sqlite3 for our database, random for some data to fill the database with, and wx for our gui obviously. First some variables are initialized. "self.reverse" and "self.oldC" are necccessary to allow for double clicking of the column header to reverse the sort (from ascending to descending, and vice versa). "self.command" is the command that is called to get data from the database. In the function "setupDB", a connection is made to a database that resides in RAM. A table is then created, saved, and then the function "self.fillDB" is called. This function uses the random module to fill the database with an assortment of integers, strings, and floats. An event, "EVT_LIST_COL_CLICK" is bound to the listCtrl, and the function to be called is "self.setupSort". It is also possible to use self.listCtrl.Bind(wx.EVT_LIST_COL_Click, self.setupSort), however wxGlade does that default to that. In self.setupSort, the column that was clicked on was is determined through event.GetColumn. Since we sort via columns, an if/elif block is used to set the command used for fetching data from the database. Further down, by comparing the column the user selected to the one they selected previously, whether to reverse the data is determined. If it is determined that it should be reversed, the SQL keyword "DESC" is appended. When using moderate table sizes, this works well. However, there is a slight amount of lag when using table sizes of above 1e5, through whether this is from the SELECT operation or the list control is uncertain.
</div>
<div>Hopefully this will help somebody</div>

"""