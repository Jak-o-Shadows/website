# -*- coding: utf-8 -*-
website = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-33695524-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

    <!-- Piwik -->
<script type="text/javascript">
var pkBaseURL = (("https:" == document.location.protocol) ? "https://sourceforge.net/userapps/piwik/jak-o-shadows/" : "http://sourceforge.net/userapps/piwik/jak-o-shadows/");
document.write(unescape("%3Cscript src='" + pkBaseURL + "piwik.js' type='text/javascript'%3E%3C/script%3E"));
</script><script type="text/javascript">
try {
var piwikTracker = Piwik.getTracker(pkBaseURL + "piwik.php", 1);
piwikTracker.trackPageView();
piwikTracker.enableLinkTracking();
} catch( err ) {}
</script><noscript><p><img src="http://sourceforge.net/userapps/piwik/jak-o-shadows/piwik.php?idsite=1" style="border:0" alt=""/></p></noscript>
<!-- End Piwik Tag -->

<!-- Start Open Web Analytics Tracker -->
<script type="text/javascript">
//<![CDATA[
var owa_baseUrl = 'http://laptimer.sourceforge.net/owa/owa/';
var owa_cmds = owa_cmds || [];
owa_cmds.push(['setSiteId', '515165129f3acb5810e6878e3db05477']);
owa_cmds.push(['trackPageView']);
owa_cmds.push(['trackClicks']);
owa_cmds.push(['trackDomStream']);

(function() {
	var _owa = document.createElement('script'); _owa.type = 'text/javascript'; _owa.async = true;
	owa_baseUrl = ('https:' == document.location.protocol ? window.owa_baseSecUrl || owa_baseUrl.replace(/http:/, 'https:') : owa_baseUrl );
	_owa.src = owa_baseUrl + 'modules/base/js/owa.tracker-combined-min.js';
	var _owa_s = document.getElementsByTagName('script')[0]; _owa_s.parentNode.insertBefore(_owa, _owa_s);
}());
//]]>
</script>
<!-- End Open Web Analytics Code -->
  
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>$title</title></head>
  
<body>$style

<table style="text-align: left; width: 100%;" border="0" cellpadding="2" cellspacing="2">

  <tbody>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td colspan="2" rowspan="1" style="vertical-align: top; text-align: center;"><a href="http://jak-o-shadows.users.sourceforge.net">Jak-o-Shadows Web</a><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/blender/blender.html">Blender</a><br>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/electronics/electronics.html">Electronics<br>
      </a>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/python/python.html">Python</a><br>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/wr/wr.html">Water Rockets</a><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td colspan="3" rowspan="1" style="vertical-align: top;"><br>$contents<br />
      <h1>Related Links</h1><br />
      <h2>First Relation</h2><br />
      <div id="first">$first</div>
      <br />
      <h2>Second Relation</h2>
      <div id="second">$second</div>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td colspan="4" rowspan="1" style="vertical-align: top;">Last update was on $time<br />All
works licensed under the GPL general public license v3, unless
otherwise noted. Content may include works based upon public domain
content.<br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
  </tbody>
</table>

<br>

<br>

</body></html>
"""

def nonCheetah(title, style, contents, time, first, second):
    t = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>

  
  <meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title>{!0}</title></head><body>{!1}

<table style="text-align: left; width: 100%;" border="0" cellpadding="2" cellspacing="2">

  <tbody>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td colspan="2" rowspan="1" style="vertical-align: top; text-align: center;"><a href="http://jak-o-shadows.users.sourceforge.net">Jak-o-Shadows Web</a><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/blender/blender.html">Blender</a><br>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/electronics/electronics.html">Electronics<br>
      </a>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/python/python.html">Python</a><br>
      </td>
      <td style="vertical-align: top;"><a href="http://jak-o-shadows.users.sourceforge.net/wr/wr.html">Water Rockets</a><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td colspan="3" rowspan="1" style="vertical-align: top;"><br>{!2}
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;"><br>
      </td>
      <div id="first">{4}</div>
<br />
<div id="second">{5}</div>
      <td colspan="4" rowspan="1" style="vertical-align: top;">Last update was on {!3}<br />All
works licensed under the GPL general public license v3, unless
otherwise noted. Content may include works based upon public domain
content.<br>
      </td>
      <td style="vertical-align: top;"><br>
      </td>
    </tr>
  </tbody>
</table>

<br>

<br>


</body></html>
""".format(title, style, contents, time, first, second)                
    return t


