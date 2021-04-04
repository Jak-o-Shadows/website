title = "Configuring Snapraid & MergerFs on Alma Linux (2021)"
contents = """



<h2>Mounting Disks</h2>
<p>Each disk (both parity and data storage) must be mounted. This is done on a permanent basis by modifying the <fstab> file. This (best) needs the disk unique identifier. Use <code># fdisk -l</code> to identify which device under <code>/dev/sd*</code> is which. Then use <code># blkid</code> to find the UUID. Note that the folders eachdisk is to be mounted in must be created. I used:
<ul>
    <li><code>/mnt/4tb_0</code></li>
    <li><code>/mnt/4tb_1</code></li>
    <li><code>/mnt/2tb_0</code></li>
</ul>
</p>

<p> My HDD were the following:
<ul>
    <li>Data Drive 0:
        <ul>
            <li>Mount point: <code>/mnt/4tb_0</code></li>
            <li>Dev location: <code>/dev/sdb</code></li>
            <li>UUID: <code>2f03fbbb-00d7-437b-a1ae-fff33fdcd212</code>
            <li>Use: Data disk 0</li>
        </ul></li>
    <li>Parity Drive 1:
        <ul>
            <li>Mount point: <code>/mnt/4tb_1</code></li>
            <li>Dev location: <code>/dev/sdd</code></li>
            <li>UUID: <code>0750d9ad-3b09-480e-83e5-25d4c7ca74dc</code>
            <li>Use: Parity disk 0. Note that this matches the size of the largest disk (4TB)</li>
        </ul></li>
    <li>Data Drive 1:
        <ul>
            <li>Mount point: <code>/mnt/2tb_0</code></li>
            <li>Dev location: <code>/dev/sda</code></li>
            <li>UUID: <code>c2c2ab41-04c7-41e8-aba0-91ba0af3be17</code>
            <li>Use: Data disk 1</li>
        </ul></li>
</ul>
</p>

<p>The following entries were added to <code>/etc/fstab</code>:</p>
<p>
<pre><code>
UUID=2f03fbbb-00d7-437b-a1ae-fff33fdcd212 /mnt/4tb_0 auto nosuid,nodev,nofail,x-gvfs-show 0 0
UUID=0750d9ad-3b09-480e-83e5-25d4c7ca74dc /mnt/4tb_1 auto nosuid,nodev,nofail,x-gvfs-show 0 0
UUID=c2c2ab41-04c7-41e8-aba0-91ba0af3be17 /mnt/2tb_0 auto nosuid,nodev,nofail,x-gvfs-show 0 0
</code></pre>
</p>

<h2>MergerFS Install and Configuration</h2>
<p>
MergerFS is used to pool the various data disks into one. As it is not (currently?) available in the Alma Linux repositories, I compiled it from source before configuring it (which was surprisingly easy).
</p>
<h3>Install</h3>
<p>Install pre-requisites: <code>su -c 'yum install glibc.* glibc-devel.* glibc-headers*'</code>.
<pre><code>
cd ~
mkdir mergerfs
git clone https://github.com/trapexit/mergerfs.git
su
# cd mergherfs
# tools/install-build-pkgs
# make rpm
</coe></pre>.
Generically it is:
<pre><code>
# rpm -i rpmbuild/RPMS/<arch>/mergerfs-<version>.<arch>.rpm
</code></pre>
But specifically:
<pre><code>
# rpm -i rpmbuild/RPMS/x86_64/mergerfs-2.32.3_26_ga02f3a6-1.el8.x86_64.rpm
</code></pre>
</p>

<h3>Install</h3>
<p>Edit the <code>fstab</code> and add: <code>/mnt/4tb_0:/mnt/2tb_0 /srv/storage fuse.mergerfs direct_io,defaults,allow_other,minfreespace=50G,fsname=mergerfs 0 0</code>. Then reboot</p>


<h2>Snapraid</h2>
<p>Snapraid does the data redundancy.</p>

<h3>Install</h3>
<p>
<pre><code>
cd ~
mkdir snapraid
cd snapraid
wget https://github.com/amadvance/snapraid/releases/download/v11.5/snapraid-11.5.tar.gz
tar xf snapraid-*.tar.gz
cd snapraid-*

./configure
make
make check
su -c 'make install'
</pre></code>

<h3>Configure</h3>
<p><code># cp snapraid.conf.example /etc/snapraid.conf</code>, and then change <code>/etc/snapraid.conf</code>:
<pre><code>
# Example configuration for snapraid

# Defines the file to use as parity storage
# It must NOT be in a data disk
# Format: "parity FILE [,FILE] ..."
parity /mnt/4tb_1/snapraid.parity

# Defines the files to use as additional parity storage.
# If specified, they enable the multiple failures protection
# from two to six level of parity.
# To enable, uncomment one parity file for each level of extra
# protection required. Start from 2-parity, and follow in order.
# It must NOT be in a data disk
# Format: "X-parity FILE [,FILE] ..."
#2-parity /mnt/diskq/snapraid.2-parity
#3-parity /mnt/diskr/snapraid.3-parity
#4-parity /mnt/disks/snapraid.4-parity
#5-parity /mnt/diskt/snapraid.5-parity
#6-parity /mnt/disku/snapraid.6-parity

# Defines the files to use as content list
# You can use multiple specification to store more copies
# You must have least one copy for each parity file plus one. Some more don't hurt
# They can be in the disks used for data, parity or boot,
# but each file must be in a different disk
# Format: "content FILE"
content /var/snapraid.content
content /mnt/4tb_0/snapraid.content
content /mnt/2tb_0/snapraid.content

# Defines the data disks to use
# The name and mount point association is relevant for parity, do not change it
# WARNING: Adding here your /home, /var or /tmp disks is NOT a good idea!
# SnapRAID is better suited for files that rarely changes!
# Format: "data DISK_NAME DISK_MOUNT_POINT"
data d1 /mnt/4tb_0/
data d2 /mnt/2tb_0/

# Excludes hidden files and directories (uncomment to enable).
#nohidden
# Defines files and directories to exclude
# Remember that all the paths are relative at the mount points
# Format: "exclude FILE"
# Format: "exclude DIR/"
# Format: "exclude /PATH/FILE"
# Format: "exclude /PATH/DIR/"
exclude *.unrecoverable
exclude /tmp/
exclude /lost+found/

# Defines the block size in kibi bytes (1024 bytes) (uncomment to enable).
# WARNING: Changing this value is for experts only!
# Default value is 256 -> 256 kibi bytes -> 262144 bytes
# Format: "blocksize SIZE_IN_KiB"
#blocksize 256

# Defines the hash size in bytes (uncomment to enable).
# WARNING: Changing this value is for experts only!
# Default value is 16 -> 128 bits
# Format: "hashsize SIZE_IN_BYTES"
#hashsize 16

# Automatically save the state when syncing after the specified amount
# of GB processed (uncomment to enable).
# This option is useful to avoid to restart from scratch long 'sync'
# commands interrupted by a machine crash.
# It also improves the recovering if a disk break during a 'sync'.
# Default value is 0, meaning disabled.
# Format: "autosave SIZE_IN_GB"
#autosave 500

# Defines the pooling directory where the virtual view of the disk
# array is created using the "pool" command (uncomment to enable).
# The files are not really copied here, but just linked using
# symbolic links.
# This directory must be outside the array.
# Format: "pool DIR"
#pool /pool

# Defines a custom smartctl command to obtain the SMART attributes
# for each disk. This may be required for RAID controllers and for
# some USB disk that cannot be autodetected.
# In the specified options, the "%s" string is replaced by the device name.
# Refers at the smartmontools documentation about the possible options:
# RAID -> https://www.smartmontools.org/wiki/Supported_RAID-Controllers
# USB -> https://www.smartmontools.org/wiki/Supported_USB-Devices
#smartctl d1 -d sat %s
#smartctl d2 -d usbjmicron %s
#smartctl parity -d areca,1/1 /dev/sg0
#smartctl 2-parity -d areca,2/1 /dev/sg0
</pre></code>

</p>

<h3>First run</h3>
<p>Run <code># snapraid sync</code>. Takes some time to run.



<h2>Sources</h2>
<p>
<ul>
    <li><a href="https://selfhostedhome.com/combining-different-sized-drives-with-mergerfs-and-snapraid/">https://selfhostedhome.com/combining-different-sized-drives-with-mergerfs-and-snapraid/</a></li>
    <li><a href="https://www.techrepublic.com/article/how-to-properly-automount-a-drive-in-ubuntu-linux/">https://www.techrepublic.com/article/how-to-properly-automount-a-drive-in-ubuntu-linux/</a></li>
    <li><a href="https://github.com/trapexit/mergerfs">https://github.com/trapexit/mergerfs</a></li>
    <li><a href="https://linuxconfig.org/install-samba-on-redhat-8">https://linuxconfig.org/install-samba-on-redhat-8</a></li>
    <li><a href="https://www.linuxtechi.com/install-configure-samba-centos-8/">https://www.linuxtechi.com/install-configure-samba-centos-8/</a></li>
</ul>
</p>

"""
style = ""
filesNeeded = []