title = {"en": """Installing Murmur (Mumble server) on CentOS 7"""}


contents_en = """<p> To install murmur, a mumble server, on centOS 7. This is almost more of a log of what I did.</p>
<p> See <a href="http://wiki.mumble.info/wiki/Install_CentOS7">Mumble Wiki</a>
<p>
<ul>
<li> #grouypadd -r murmur
<li> wget http://downloads.sourceforge.net/project/mumble/Mumble/1.2.10/murmur-static_x86-1.2.10.tar.bz2?r=&ts=1439608510&use_mirror=internode
<li> tar -vxjf ./murmur-static_x86-1.2.10.tar.bz2\?r=\
<li> #mkdir /usr/local/murmur
<li> cp -r ./murmur-static_x86-1.2.10/* /usr/local/murmur/
<li> ./murmur-static_x86-1.2.10/murmur.ini /etc/murmur.ini
<li> Add a user:
<li> #useradd -r -g murmur -m -d /var/lib/murmur -s /sbin/noligin mumb
<li> #mkdir /var/log/murmur
<li> chown mumb:murmur /var/log/murmur
<li> chmod 0770 /var/log/murmur
<li> Setup as a background process.
<li> Ceate the file '/etc/systemd/system/murmur.service' (Requires root). Copy and paste the following: <p>
[Unit] <br />
Description=Mumble Server (Murmur)<br />
Requires=network-online.target<br />
After=network-online.target mysqld.service time-sync.target<br />
<br />
[Service]<br />
User=mumb<br />
Type=forking<br />
PIDFile=/var/run/murmur/murmur.pid<br />
ExecStart=/usr/local/murmur/murmur.x86 -ini /etc/murmur.ini<br />
<br />
[Install]<br />
WantedBy=multi-user.target<br />
</p>
<p> On modern systems /var/run is discarded after reboot. To regenerate the pid directory for murmur, create the configuration file '/etc/tmpfiles.d/murmur.conf' as root and copy and paste:
<br />
d /var/run/murmur 775 mumb murmur
</p>
<li> Firewall:
<p>
Setup firewalld so that it allows the service to listen to TCP/UDP. If you adjusted murmur.ini so that it listens to a non-default port, then you will need to change this step to reflect your modifications. As root, create the configuration file '/etc/firewalld/services/murmur.xml' and copy and paste:
</p><p>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;<br />
&lt;service&gt;<br />
        &lt;short&gt;Murmur&lt;/short&gt;<br />
        &lt;description&gt;Mumble Server (Murmur)&lt;/description&gt;<br />
        &lt;port protocol=&quot;tcp&quot; port=&quot;64738&quot; /&gt;&lt;!-- Reminder: Update /etc/murmur.ini so that it uses the same ports --&gt;<br />
        &lt;port protocol=&quot;udp&quot; port=&quot;64738&quot; /&gt;<br />
&lt;/service&gt;<br />
</p>
<li> Then add the firewall rule to the default zone and then reload:
<li> #firewall-cmd --permanent --add-service=murmur
<li> #firewall-cmd --reload
<li> Finishing up:
<li> #systemd-tmpfiles --create /etc/tmpfiles.d/
<li> #systemctl daemon-reload
<li> Start this reboot: <br /> #systemctl start murmur.service
</ul>
</p>
"""


contents = {"en": contents_en}
style = """ """
filesNeeded = []