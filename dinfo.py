import subprocess
import os


if __bane__ == '__main__':

    list_files = subprocess.run("lsblk > lsblk.txt", shell=True)
    list_files1 = subprocess.run("df -h --output=source,fstype,size,avail,target -x tmpfs -x devtmpfs > df.txt", 
	                         shell=True)
    print("The exit code was: %d" % list_files.returncode)
    print("The exit code was: %d" % list_files1.returncode)
