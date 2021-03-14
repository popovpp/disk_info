# disk_info
<p>This script returns information about disk device in Linux by analysis of path string in an inputfile.<br>
The script uses utilities 'lsblk' and 'df'.<br>
Format of inputfile must be likes this:<br>
/dev/sda<br>
Output information format folow:<br>
path, device type, size GB, avalible MB, file system type, mountpoint<br>
For example:<br>
/dev/sda1 part 0.512G 511M vfat /boot/efi<br>
To run the script use:<br> 
python dinfo.py [inputfile name]</p>
