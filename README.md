# disk_info
This script returns information about disk device in Linux by analysis of path string in an inputfile.
The script uses utilities 'lsblk' and 'df'.
Format of inputfile must be likes this:
/dev/sda
Output information format folow:
path, device type, size GB, avalible MB, file system type, mountpoint
For example:
/dev/sda1 part 0.512G 511M vfat /boot/efi
To run the script use: 
python dinfo.py [inputfile name]
